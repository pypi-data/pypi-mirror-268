import logging
import os
import select
import subprocess
import time
from threading import Event as TEvent
from threading import Thread
from typing import Literal, cast

from Xlib import display

from hhd.plugins import Context, Emitter

from .controllers import OverlayWriter
from .overlay import find_overlay_exe, inject_overlay
from .x11 import (find_hhd, find_steam, get_gamescope_displays,
                  get_overlay_display, hide_hhd, prepare_hhd, process_events,
                  register_changes, show_hhd, update_steam_values)

logger = logging.getLogger(__name__)
Command = Literal[
    "close_now",
    "close",
    "open_qam",
    "open_qam_if_closed",
    "open_expanded",
    "open_notification",
]
Status = Literal["closed", "qam", "expanded", "notification"]

GUARD_CHECK = 0.5
STARTUP_MAX_DELAY = 10
LOOP_SLEEP = 0.05


def loop_manage_overlay(
    disp: display.Display,
    proc: subprocess.Popen,
    emit: Emitter,
    writer: OverlayWriter,
    should_exit: TEvent,
):
    try:
        status: Status = "closed"

        assert proc.stderr and proc.stdout

        fd_out = proc.stdout.fileno()
        fd_err = proc.stderr.fileno()
        os.set_blocking(fd_out, False)
        os.set_blocking(fd_err, False)
        fd_disp = disp.fileno()

        # Give electron time to warmup
        start = time.perf_counter()
        curr = start
        while (
            curr - start < STARTUP_MAX_DELAY
            and not find_hhd(disp)
            and not should_exit.is_set()
        ):
            time.sleep(GUARD_CHECK)
            curr = time.perf_counter()

        hhd = find_hhd(disp)
        steam = find_steam(disp)
        old = None
        shown = False

        if hhd:
            logger.info(f"UI window found in gamescope, starting handler.")
            prepare_hhd(disp, hhd)
        if steam:
            register_changes(disp, steam)

        while not should_exit.is_set():
            if not hhd:
                logger.error(f"UI Window not found, exitting overlay.")
                break
            if not steam:
                logger.error(f"Steam window not found, exitting overlay.")
                break

            start = time.perf_counter()
            select.select([fd_out, fd_err, fd_disp], [], [], GUARD_CHECK)

            if proc.poll() is not None:
                logger.warning(f"Overlay stopped (steam may have restarted). Closing.")
                return

            # If steam tries to appear while the overlay is active
            # yank its focus
            process_events(disp)
            if shown:
                old, was_shown = update_steam_values(disp, steam, old)
                if was_shown:
                    show_hhd(disp, hhd, steam)
                    logger.warning("Steam opened, hiding it.")

            # Process system logs
            while True:
                l = proc.stderr.readline()[:-1]
                if not l:
                    break
                logger.info(f"UI: {l}")

            # Update overlay status
            while True:
                cmd = proc.stdout.readline()[:-1]
                if not cmd:
                    break
                if cmd.startswith("stat:"):
                    status = cast(Status, cmd[5:])
                    if status == "closed":
                        if shown:
                            hide_hhd(disp, hhd, steam, old)
                            old = None
                            writer.reset()
                            # Prevent grabbing when the UI is not shown
                            emit.grab(False)
                        shown = False
                    else:
                        if not shown:
                            old, _ = update_steam_values(disp, steam, None)
                            show_hhd(disp, hhd, steam)
                            writer.reset()
                        shown = True
                elif cmd.startswith("grab:"):
                    enable = cmd[5:]
                    emit.grab(enable == "enable")

            # Sleep a bit to avoid running too often
            # Only do so if the earlier sleep was too short to avoid having
            # steam slipping in the UI and flashing the screen
            elapsed = time.perf_counter() - start
            if elapsed < LOOP_SLEEP:
                time.sleep(LOOP_SLEEP - elapsed)
    except Exception as e:
        logger.warning(f"The overlay process ended with an exception:\n{e}")
    finally:
        logger.info(f"Stopping overlay process.")
        proc.kill()
        proc.wait()


class OverlayService:
    def __init__(self, ctx: Context, emit: Emitter) -> None:
        self.ctx = ctx
        self.started = False
        self.t = None
        self.should_exit = None
        self.emit = emit

    def _start(self):
        # Should not be called by outsiders
        # requires special permissions and error handling by update
        if self.started:
            return True
        logger.info("Attempting to launch overlay.")

        exe = find_overlay_exe(self.ctx)
        if not exe:
            logger.warning("Overlay is not installed, not launching.")
            return False
        logger.info(f"Found overlay executable '{exe}'")

        displays = get_gamescope_displays()
        if not displays:
            logger.warning("Could not find overlay displays, gamescope is not active.")
            return False
        logger.debug(f"Found the following gamescope displays: {displays}")

        res = get_overlay_display(displays, self.ctx)
        if not res:
            logger.error(
                f"Could not find overlay display in gamescope displays. This should never happen."
            )
            return False
        disp, name = res
        logger.debug(f"Overlay display is the folling: DISPLAY={name}")

        self.proc = inject_overlay(exe, name, self.ctx)
        self.writer = OverlayWriter(self.proc.stdin)
        self.emit.register_intercept(self.writer)
        self.should_exit = TEvent()
        self.t = Thread(
            target=loop_manage_overlay,
            args=(disp, self.proc, self.emit, self.writer, self.should_exit),
        )
        self.t.start()

        self.started = True
        logger.info("Overlay launched.")
        return True

    def close(self):
        if self.should_exit and self.t:
            self.should_exit.set()
            self.t.join()
        self.should_exit = None
        self.t = None
        self.started = False

    def is_healthy(self):
        if not self.t or not self.should_exit:
            logger.error("'is_healthy' called before 'start'")
            return False

        if not self.t.is_alive():
            logger.error("Overlay thread died")
            return False

        return True

    def update(self, cmd: Command, init: bool):
        # Accessing the user's display requires the user's priviledges
        if not self.started and not init:
            # This function is called with QAM single presses and guide presses
            # do not initialize for those.
            return
        try:
            if not self._start():
                return
            if not self.is_healthy():
                logger.warning(f"Overlay service died, attempting to restart.")
                self.close()
                if not self._start():
                    logger.warning(f"Restarting overlay failed.")
                    return

            if not self.proc:
                logger.error("Overlay subprocess is null. Should never happen.")
                return

            self.writer.write(f"\ncmd:{cmd}\n")
        except Exception as e:
            logger.error(f"Failed launching overlay with error:\n{e}")
            self.close()

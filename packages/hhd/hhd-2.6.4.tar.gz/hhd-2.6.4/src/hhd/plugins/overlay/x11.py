import logging
import subprocess
import time
from select import select
from threading import Event as TEvent
from typing import Any, NamedTuple, Sequence

import Xlib
from Xlib import XK, X, Xatom, display, error
from Xlib.ext.xtest import fake_input

from hhd.plugins import Emitter
from hhd.utils import restore_priviledge, switch_priviledge

logger = logging.getLogger(__name__)

X11_DIR = b"/tmp/.X11-unix/"


class CachedValues(NamedTuple):
    overlay: bool
    focus: bool
    notify: bool
    touch: int | None


class QamHandler:

    def __init__(
        self, ctx=None, force_disp: str | None = None, compat_send: bool = True
    ) -> None:
        self.disp = None
        self.ctx = ctx
        self.force_disp = force_disp
        self.compat_send = compat_send

    def _register_display(self):
        self.close()
        try:
            if self.force_disp:
                res = display.Display(self.force_disp), self.force_disp
            else:
                res = get_overlay_display(get_gamescope_displays(), self.ctx)
            if not res:
                logger.info(
                    f"Could not find gamescope display, sending compatibility QAM."
                )
                return False
            self.disp, name = res
            logger.info(f"Registering display {name} to send QAM events to.")
            return True
        except Exception as e:
            logger.info(f"Error while registering Gamescope display for QAM:\n{e}.")
            return False

    def _send_qam(self, expanded=False):
        try:
            disp = self.disp
            if not disp:
                return False
            get_key = lambda k: disp.keysym_to_keycode(XK.string_to_keysym(k))
            KCTRL = get_key("Control_L")
            KEY = get_key("1" if expanded else "2")

            # Checking for steam seemed to work, but blanket sending the command
            # with a compatibility QAM at first works the same and this looks
            # fragile
            # steam = find_steam(disp)
            # if not steam:
            #     logger.info(f"Could not find Steam (?). Sending compatibility QAM.")
            #     return False

            fake_input(disp, X.KeyPress, KCTRL)  # , root=steam)
            fake_input(disp, X.KeyPress, KEY)  # , root=steam)
            disp.sync()
            fake_input(disp, X.KeyRelease, KCTRL)  # , root=steam)
            fake_input(disp, X.KeyRelease, KEY)  # , root=steam)
            disp.sync()
            logger.info(f"Sent QAM event directly to gamescope.")
            return True
        except Exception as e:
            logger.warning(
                f"Could not send QAM to Gamescope with error:\n{e}\nSending compatibility QAM."
            )
            return False

    def __call__(self, expanded=False) -> Any:
        if self._send_qam(expanded):
            return True
        # Steam fails to open QAM with ctrl+2 the first time
        # So send compatibility QAM if we have to register display
        if self._register_display() and self.compat_send:
            logger.info(
                "Sending compatibility QAM as first QAM, as display was registered now."
            )
        if not self.compat_send:
            return self._send_qam(expanded)
        return False

    def close(self):
        if self.disp:
            try:
                self.disp.close()
                self.disp = None
            except Exception:
                pass


def get_gamescope_displays():
    """Returns X11 UNIX sockets from gamescope opened under /tmp"""
    files = subprocess.run(["lsof", "-c", "gamescope-wl", "-Fn"], capture_output=True)
    out = []
    for ln in files.stdout.splitlines():
        if len(ln) < 1:
            continue
        ln = ln[1:]

        if not ln.startswith(X11_DIR):
            continue

        fn = ln.split(b" ")[0]
        disp = ":" + fn[len(X11_DIR) + 1 :].decode()
        out.append(disp)
    return out


def get_overlay_display(displays: Sequence[str], ctx=None):
    """Probes the provided gamescope displays to find the overlay one."""

    # FIXME: Fix authentication without priviledge deescalation
    if ctx:
        old = switch_priviledge(ctx, False)
    else:
        old = None

    try:
        for disp in displays:
            try:
                d = display.Display(disp)

                atoms = [d.get_atom_name(v) for v in d.screen().root.list_properties()]
                if "GAMESCOPE_FOCUSED_WINDOW" in atoms:
                    return d, disp

                d.close()
            except Exception:
                pass
    finally:
        if old:
            restore_priviledge(old)


def find_win(display: display.Display, win: list[str], atoms: list[str] = []):
    n = display.get_atom("WM_CLASS")
    a_ids = [display.get_atom(a, only_if_exists=True) for a in atoms]

    for w in display.screen().root.query_tree().children:
        # Check the window has the proper class
        v = w.get_property(n, Xatom.STRING, 0, 50)
        if not v:
            continue
        if not v.value:
            continue

        # Check the window has all the required atoms
        for a_id in a_ids:
            if not w.get_property(a_id, Xatom.STRING, 0, 50):
                return

        classes = [c.decode() for c in v.value.split(b"\00") if c]
        found = True
        for val in win:
            if val not in classes:
                found = False

        if found:
            return w


def register_changes(display, win):
    win.change_attributes(event_mask=Xlib.X.PropertyChangeMask)
    display.flush()
    display.sync()


def find_hhd(display: display.Display):
    return find_win(display, ["dev.hhd.hhd-ui"])


def find_steam(display: display.Display):
    return find_win(display, ["steamwebhelper", "steam"])


def print_data(display: display.Display):
    for w in (find_hhd(display), find_steam(display), display.screen().root):
        if not w:
            continue
        for p in w.list_properties():
            req = w.get_property(p, Xatom.CARDINAL, 0, 100)
            if req:
                v = list(req.value) if req.value else None
            else:
                v = None
            print(f"{p:4d}-{display.get_atom_name(p):>40s}: {v}")
        print()


def print_debug(display: display.Display, args: list[str] = []):
    d = display
    r = display.screen().root

    if "noatoms" not in args:
        print("ATOMS:")
        for v in r.list_properties():
            print(f"{v: 4d}: {d.get_atom_name(v)}")

    if "root" in args:
        windows = [r]
    else:
        windows = [r, *r.query_tree().children]

    print()
    print("WINDOWS:")
    for i, w in enumerate(windows):
        print(f"\n{i:02d}:", end="")
        for p in w.list_properties():
            n = d.get_atom_name(p)
            if "WM_NAME" == n:
                print(f" '{w.get_property(p, Xatom.STRING, 0, 100).value.decode()}'")
                break
        else:
            print(" no name")

        for p in w.list_properties():
            n = d.get_atom_name(p)
            if "STEAM" in n or "GAMESCOPE" in n:
                print(
                    f"> {n}: {list(w.get_property(p, Xatom.CARDINAL, 0, 15).value)},",
                )
        for p in w.list_properties():
            n = d.get_atom_name(p)
            if "STEAM" not in n and "GAMESCOPE" not in n:
                print(
                    f"- {n}: {list(w.get_property(p, Xatom.CARDINAL, 0, 15).value) or w.get_property(p, Xatom.STRING, 0, 15).value},",
                )


def prepare_hhd(display, hhd):
    hhd.change_property(display.get_atom("STEAM_GAME"), Xatom.CARDINAL, 32, [5335])
    hhd.change_property(display.get_atom("STEAM_NOTIFICATION"), Xatom.CARDINAL, 32, [0])
    hhd.change_property(display.get_atom("STEAM_BIGPICTURE"), Xatom.CARDINAL, 32, [1])
    display.flush()
    display.sync()


def process_events(disp):
    try:
        found = False
        for _ in range(disp.pending_events()):
            ev = disp.next_event()
            if ev and hasattr(ev, "atom") and "STEAM" in disp.get_atom_name(ev.atom):
                found = True
        return found
    except Exception as e:
        logger.warning(f"Failed to process display events with error:\n{e}")
    return True


def update_steam_values(display, steam, old: CachedValues | None):
    stat_focus = display.get_atom("STEAM_INPUT_FOCUS")
    stat_overlay = display.get_atom("STEAM_OVERLAY")
    stat_notify = display.get_atom("STEAM_NOTIFICATION")
    stat_click = display.get_atom("STEAM_TOUCH_CLICK_MODE")

    def was_set(v):
        prop = steam.get_property(v, Xatom.CARDINAL, 0, 15)
        return prop and prop.value and bool(prop.value[0])

    new_focus = was_set(stat_focus)
    new_overlay = was_set(stat_overlay)
    new_notify = was_set(stat_notify)

    # Use some weird logic to get previous touch value
    # Essentially, only remember that value if it was set and different than TARGET_TOUCH
    r = display.screen().root
    prop = r.get_property(stat_click, Xatom.CARDINAL, 0, 15)
    touch_was_set = prop and prop.value and prop.value[0] != TARGET_TOUCH
    touch_val = prop.value[0] if touch_was_set else None
    if touch_val is None and old and old.touch is not None:
        touch_val = old.touch

    out = CachedValues(
        focus=new_focus or (old.focus if old else False),
        overlay=new_overlay or (old.overlay if old else False),
        notify=new_notify or (old.notify if old else False),
        touch=touch_val,
    )
    return out, new_focus or new_overlay or new_notify


TARGET_TOUCH = 4


def show_hhd(display, hhd, steam):
    stat_focus = display.get_atom("STEAM_INPUT_FOCUS")
    stat_overlay = display.get_atom("STEAM_OVERLAY")
    stat_notify = display.get_atom("STEAM_NOTIFICATION")
    stat_click = display.get_atom("STEAM_TOUCH_CLICK_MODE")

    # If steam set the touch value to something else, try to override it with 1
    r = display.screen().root
    prop = r.get_property(stat_click, Xatom.CARDINAL, 0, 15)
    touch_was_set = prop and prop.value

    hhd.change_property(stat_focus, Xatom.CARDINAL, 32, [1])
    hhd.change_property(stat_overlay, Xatom.CARDINAL, 32, [1])
    steam.change_property(stat_focus, Xatom.CARDINAL, 32, [0])
    steam.change_property(stat_overlay, Xatom.CARDINAL, 32, [0])
    steam.change_property(stat_notify, Xatom.CARDINAL, 32, [0])

    if touch_was_set:
        # Give it a bit of time before setting the touch target to avoid steam
        # messing with it
        display.flush()
        display.sync()
        time.sleep(0.2)
        r.change_property(stat_click, Xatom.CARDINAL, 32, [TARGET_TOUCH])

    display.flush()
    display.sync()


def hide_hhd(display, hhd, steam, old: CachedValues | None):
    stat_focus = display.get_atom("STEAM_INPUT_FOCUS")
    stat_overlay = display.get_atom("STEAM_OVERLAY")
    stat_notify = display.get_atom("STEAM_NOTIFICATION")
    stat_click = display.get_atom("STEAM_TOUCH_CLICK_MODE")

    # Set values
    hhd.change_property(stat_focus, Xatom.CARDINAL, 32, [0])
    hhd.change_property(stat_overlay, Xatom.CARDINAL, 32, [0])

    # Restore steam
    if old:
        if old.focus:
            steam.change_property(stat_focus, Xatom.CARDINAL, 32, [1])
        if old.overlay:
            steam.change_property(stat_overlay, Xatom.CARDINAL, 32, [1])
        if old.notify:
            steam.change_property(stat_notify, Xatom.CARDINAL, 32, [1])
        if old.touch is not None:
            display.screen().root.change_property(
                stat_click, Xatom.CARDINAL, 32, [old.touch]
            )

    display.flush()
    display.sync()


def monitor_gamescope(emit: Emitter, ctx, should_exit: TEvent):
    GAMESCOPE_WAIT = 2
    GAMESCOPE_GUARD = 1

    should_exit = TEvent()

    while not should_exit.is_set():
        # Wait for gamescope
        try:
            res = get_overlay_display(get_gamescope_displays(), ctx)
            if not res:
                time.sleep(GAMESCOPE_WAIT)
                continue

            d, name = res
            logger.info(f"Found gamescope display {name}")
            r = d.screen().root
            r.change_attributes(event_mask=X.PropertyChangeMask)
            fn = d.fileno()
            atom = d.get_atom("GAMESCOPE_FOCUSED_APP_GFX")
            old = None

            while not should_exit.is_set():
                rs = select([fn], [], [], GAMESCOPE_GUARD)[0]
                if not rs:
                    continue

                process_events(d)

                val = r.get_property(atom, Xatom.CARDINAL, 0, 5)
                if not val or not val.value:
                    continue

                game = val.value[0]
                if old != game:
                    old = game
                    logger.warning(game)

        except Exception as e:
            logger.warning(f"Lost connection to gamescope. Did steam exit? Error:\n{e}")
            time.sleep(GAMESCOPE_WAIT)

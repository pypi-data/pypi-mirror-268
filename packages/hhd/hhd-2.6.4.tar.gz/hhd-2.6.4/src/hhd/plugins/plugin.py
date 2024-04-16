import getpass
import logging
import os
import subprocess
from typing import Any, Literal, Mapping, NamedTuple, Protocol, Sequence, TypedDict

from hhd.controller import Axis, Button, Configuration, ControllerEmitter, SpecialEvent

from .conf import Config
from .settings import HHDSettings

logger = logging.getLogger(__name__)

STEAM_PID = "~/.steam/steam.pid"


class Context(NamedTuple):
    euid: int = 0
    egid: int = 0
    uid: int = 0
    gid: int = 0
    name: str = "root"
    # scratch: str = ""


class SettingsEvent(TypedDict):
    type: Literal["settings"]


class PowerEvent(TypedDict):
    type: Literal["acpi"]
    event: Literal["ac", "dc", "tdp", "battery"]


class ProfileEvent(TypedDict):
    type: Literal["profile"]
    name: str
    config: Config | None


class ApplyEvent(TypedDict):
    type: Literal["apply"]
    name: str


class ConfigEvent(TypedDict):
    type: Literal["state"]
    config: Config


class InputEvent(TypedDict):
    type: Literal["input"]
    controller_id: int

    btn_state: Mapping[Button, bool]
    axis_state: Mapping[Axis, bool]
    conf_state: Mapping[Configuration, Any]


Event = (
    ConfigEvent
    | InputEvent
    | ProfileEvent
    | ApplyEvent
    | SettingsEvent
    | SpecialEvent
    | PowerEvent
)


class Emitter(ControllerEmitter):
    def __call__(self, event: Event | Sequence[Event]) -> None:
        pass


class HHDPlugin:
    name: str
    priority: int
    log: str

    def open(
        self,
        emit: Emitter,
        context: Context,
    ):
        pass

    def settings(self) -> HHDSettings:
        return {}

    def validate(self, tags: Sequence[str], config: Any, value: Any):
        return False

    def prepare(self, conf: Config):
        pass

    def update(self, conf: Config):
        pass

    def notify(self, events: Sequence[Event]):
        pass

    def close(self):
        pass


class HHDAutodetect(Protocol):
    def __call__(self, existing: Sequence[HHDPlugin]) -> Sequence[HHDPlugin]:
        raise NotImplementedError()


class HHDLocale(TypedDict):
    dir: str
    domain: str
    priority: int


class HHDLocaleRegister(Protocol):
    def __call__(self) -> Sequence[HHDLocale]:
        raise NotImplementedError()


def get_context(user: str | None) -> Context | None:
    try:
        uid = os.getuid()
        gid = os.getgid()

        if not user:
            if not uid:
                print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print(
                    "Running as root without a specified user (`--user`). Configs will be placed at `/root/.config`."
                )
                print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return Context(uid, gid, uid, gid, getpass.getuser())

        euid = int(
            subprocess.run(
                ["id", "-u", user], capture_output=True, check=True
            ).stdout.decode()
        )
        egid = int(
            subprocess.run(
                ["id", "-g", user], capture_output=True, check=True
            ).stdout.decode()
        )

        if (uid or gid) and (uid != euid or gid != egid):
            print(
                f"The user specified with --user is not the user this process was started with."
            )
            return None

        return Context(euid, egid, uid, gid, user)
    except subprocess.CalledProcessError as e:
        print(f"Getting the user uid/gid returned an error:\n{e.stderr.decode()}")
        return None
    except Exception as e:
        print(f"Failed getting permissions with error:\n{e}")
        return None


def switch_priviledge(p: Context, escalate=False):
    uid = os.geteuid()
    gid = os.getegid()

    if escalate:
        os.seteuid(p.uid)
        os.setegid(p.gid)
    else:
        os.setegid(p.egid)
        os.seteuid(p.euid)

    return uid, gid


def restore_priviledge(old: tuple[int, int]):
    uid, gid = old
    # Try writing group first in case of root
    # and fail silently
    try:
        os.setegid(gid)
    except Exception:
        pass
    os.seteuid(uid)
    os.setegid(gid)
    pass


def expanduser(path: str, user: int | str | Context | None = None):
    """Expand ~ and ~user constructions.  If user or $HOME is unknown,
    do nothing.

    Modified from the python implementation to support using the target userid/user."""

    path = os.fspath(path)

    if not path.startswith("~"):
        return path

    i = path.find("/", 1)
    if i < 0:
        i = len(path)
    if i == 1:
        if "HOME" in os.environ and not user:
            # Fallback to environ only if user not set
            userhome = os.environ["HOME"]
        else:
            try:
                import pwd
            except ImportError:
                # pwd module unavailable, return path unchanged
                return path
            try:
                if not user:
                    userhome = pwd.getpwuid(os.getuid()).pw_dir
                elif isinstance(user, int):
                    userhome = pwd.getpwuid(user).pw_dir
                elif isinstance(user, Context):
                    userhome = pwd.getpwuid(user.euid).pw_dir
                else:
                    userhome = pwd.getpwnam(user).pw_dir
            except KeyError:
                # bpo-10496: if the current user identifier doesn't exist in the
                # password database, return the path unchanged
                return path
    else:
        try:
            import pwd
        except ImportError:
            # pwd module unavailable, return path unchanged
            return path
        name = path[1:i]
        try:
            pwent = pwd.getpwnam(name)
        except KeyError:
            # bpo-10496: if the user name from the path doesn't exist in the
            # password database, return the path unchanged
            return path
        userhome = pwent.pw_dir

    root = "/"
    userhome = userhome.rstrip(root)
    return (userhome + path[i:]) or root


def fix_perms(fn: str, ctx: Context):
    os.chown(fn, ctx.euid, ctx.egid)


def is_steam_gamepad_running(ctx: Context | None):
    pid = None
    try:
        with open(expanduser(STEAM_PID, ctx)) as f:
            pid = f.read().strip()

        steam_cmd_path = f"/proc/{pid}/cmdline"
        if not os.path.exists(steam_cmd_path):
            return False

        # Use this and line to determine if Steam is running in DeckUI mode.
        with open(steam_cmd_path, "rb") as f:
            steam_cmd = f.read()
        is_deck_ui = b"-gamepadui" in steam_cmd
        if not is_deck_ui:
            return False
    except Exception:
        return False
    return True

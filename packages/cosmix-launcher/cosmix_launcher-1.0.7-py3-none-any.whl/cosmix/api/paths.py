import os
from os.path import join


__all__ = (
    "LOCAL_PATH",
    "WORK_DIR",
    "DEPS",
    "INSTANCES",
    "path_to_cr",
)


LOCAL_PATH = (
    os.environ.get("APPDATA") or
    os.environ.get("XDG_DATA_HOME") or
    join(os.environ["HOME"], ".local", "share")
)

WORK_DIR   = join(LOCAL_PATH, "cosmix")
DEPS       = join(WORK_DIR, "deps")
INSTANCES  = join(WORK_DIR, "instances")


def path_to_cr(version: str) -> str:
    return join(DEPS, "cosmic-reach", version + ".jar")


def update_work_dir(path: str):
    global WORK_DIR, DEPS, INSTANCES
    WORK_DIR   = path
    DEPS       = join(WORK_DIR, "deps")
    INSTANCES  = join(WORK_DIR, "instances")

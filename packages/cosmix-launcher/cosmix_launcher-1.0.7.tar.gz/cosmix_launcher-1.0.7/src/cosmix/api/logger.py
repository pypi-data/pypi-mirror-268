from . import config
# import getpass
import os


__all__ = (
    "LEVELS",
    "sanatize_username",
    "log",
    "error",
    "warn",
    "info",
    "debug",
)


LEVELS = {
    "error": "\u001b[31m",
    "warn":  "\u001b[33m",
    "info":  "\u001b[36m",
    "debug": "\u001b[34m",
}

_sanatization_mode = _sanatized_username = _colored_logs = None


# Sadly there is no easy way for me to sanatize logging from the game's process because
# the Python process is replaced with the Java one when CR is launched.
def sanitize_username(string: str | list[str]) -> str:
    global _sanatization_mode, _sanatized_username

    if _sanatization_mode is None:
        _sanatization_mode = config.get_config()["logging"]["sanatization_mode"]

    if _sanatization_mode == "none":
        return string

    if type(string) == list:
        return [sanatize_username(s) for s in string]

    if _sanatization_mode == "sanatize":
        if _sanatized_username is None:
            _sanatized_username = config.get_config()["logging"]["sanatized_username"]
        replace_with = _sanatized_username
    elif _sanatization_mode == "replace":
        replace_with = "~"

    return string.replace(os.path.expanduser("~"), replace_with)


def log(text: str, level: str):
    global _colored_logs
    if _colored_logs is None:
        _colored_logs = config.get_config()["logging"]["colored_logs"]

    level_text = (LEVELS[level] + level + "\u001b[0m") if _colored_logs else level
    print(f"[{level_text}]: {sanitize_username(text)}")


def error(text: str): log(text, "error")
def warn(text: str):  log(text, "warn")
def info(text: str):  log(text, "info")
def debug(text: str): log(text, "debug")

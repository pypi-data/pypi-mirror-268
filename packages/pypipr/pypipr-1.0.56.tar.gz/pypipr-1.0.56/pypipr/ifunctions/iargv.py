import sys


def iargv(key: int, cast=None, on_error=None):
    try:
        v = sys.argv[key]
        if cast:
            return cast(v)
        else:
            return v
    except Exception:
        return on_error

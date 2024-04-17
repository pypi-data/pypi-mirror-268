from ..ibuiltins.WINDOWS import WINDOWS
from ..iconsole.console_run import console_run
from ..ifunctions.ijoin import ijoin
from ..ifunctions.iopen import iopen


def pip_freeze_without_version(filename=None):
    """
    Memberikan list dari dependencies yang terinstall tanpa version.
    Bertujuan untuk menggunakan Batteries Included Python.

    ```py
    print(pip_freeze_without_version())
    ```
    """
    run = console_run("PIP Freeze", "pip list --format=freeze", capture_output=True)

    text = run.stdout
    if WINDOWS:
        text = text.decode()

    res = ijoin((i.split("=")[0] for i in text.splitlines()), separator="\n")

    if filename:
        return iopen(filename, data=res)

    return res


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv

    print(pip_freeze_without_version(iargv(1)))

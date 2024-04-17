from ..iconsole.console_run import console_run


def poetry_update_version(mayor=False, minor=False, patch=False):
    """
    Update versi pada pyproject.toml menggunakan poetry

    ```py
    poetry_update_version()
    ```
    """
    if mayor:
        console_run("Update version mayor", "poetry version mayor")
    if minor:
        console_run("Update version minor", "poetry version minor")
    if patch:
        console_run("Update version patch", "poetry version patch")


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv

    poetry_update_version(iargv(1, int), iargv(2, int), iargv(3, int))

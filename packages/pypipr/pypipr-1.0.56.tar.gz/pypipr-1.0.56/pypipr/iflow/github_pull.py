from ..iconsole.console_run import console_run


def github_pull():
    """
    Menjalankan command `git pull`

    ```py
    github_pull()
    ```
    """
    console_run("Git Pull", "git pull")


if __name__ == "__main__":
    github_pull()

from ..iconsole.console_run import console_run
from ..iconsole.print_colorize import print_colorize
from ..iconsole.print_log import print_log


def github_push(commit_msg=None):
    """
    Menjalankan command status, add, commit dan push

    ```py
    github_push('Commit Message')
    ```
    """

    def console_input(prompt, default):
        print_colorize(prompt, text_end="")
        if default:
            print(default)
            return default
        else:
            return input()

    print_log("Menjalankan Github Push")
    console_run("Checking files", "git status")
    msg = console_input("Commit Message if any or empty to exit : ", commit_msg)
    if msg:
        console_run("Mempersiapkan files", "git add .")
        console_run("Menyimpan files", f'git commit -m "{msg}"')
        console_run("Mengirim files", "git push")
    print_log("Selesai Menjalankan Github Push")


if __name__ == "__main__":
    github_push()

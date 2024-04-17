import pathlib


def create_folder(folder_name):
    """
    Membuat folder.
    Membuat folder secara recursive dengan permission.

    ```py
    create_folder("contoh_membuat_folder")
    create_folder("contoh/membuat/folder/recursive")
    create_folder("./contoh_membuat_folder/secara/recursive")
    ```
    """
    pathlib.Path(folder_name).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv

    if i := iargv(1):
        create_folder(i)

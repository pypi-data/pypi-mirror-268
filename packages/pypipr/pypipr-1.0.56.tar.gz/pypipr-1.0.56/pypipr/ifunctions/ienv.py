from ..ibuiltins.LINUX import LINUX
from ..ibuiltins.WINDOWS import WINDOWS


def ienv(on_windows=None, on_linux=None):
    """
    Mengambalikan hasil berdasarkan environment dimana program dijalankan

    ```py
    getch = __import__(ienv(on_windows="msvcrt", on_linux="getch"))

    inherit = ienv(
        on_windows=[BaseForWindows, BaseEnv, object],
        on_linux=[SpecialForLinux, BaseForLinux, BaseEnv, object]
    )

    class ExampleIEnv(*inherit):
        pass
    ```
    """
    if WINDOWS:
        return on_windows
    if LINUX:
        return on_linux
    raise Exception("Environment tidak diketahui.")

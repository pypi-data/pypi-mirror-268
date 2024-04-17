from ..ibuiltins.is_iterable import is_iterable
from ..ibuiltins.WINDOWS import WINDOWS
from .print_to_last_line import print_to_last_line
from .text_colorize import text_colorize


def choices(iterator, title=None, prompt="", default=None):
    """
    Memudahkan dalam membuat pilihan untuk user dalam tampilan console

    ```py
    a = choices("ini hanya satu pilihan")
    b = choices(
        {
            "sedan": "audi",
            "suv": "volvo",
            "truck": "tesla",
        },
        title="Car Model",
        prompt="Pilih Mobil : ",
    )
    c = choices(
        iscandir(recursive=False),
        title="List File dan Folder",
        prompt="Pilih File atau Folder : ",
    )
    ```
    """

    def build_iterator(iterator):
        if not is_iterable(iterator):
            iterator = [iterator]
        if not isinstance(iterator, dict):
            iterator = dict(enumerate(iterator))
        return iterator

    def print_choices(dictionary, title=None):
        if title:
            print(title)
        for k, v in dictionary.items():
            print(f"[{k}] {v}")

    def input_choices(prompt):
        i = input(prompt)
        if WINDOWS:
            i = i.decode()
        if i.isdigit():
            i = int(i)
        return i

    def return_choices(iterator, key, on_error):
        try:
            result = iterator[key]
        except Exception:
            result = on_error
        return result

    d = build_iterator(iterator)
    print_choices(d, title)
    key = input_choices(prompt)
    result = return_choices(d, key, default)
    r = text_colorize(result)
    print_to_last_line(f"{prompt}{key} [{r}]")
    return result

import re

from ..ifunctions.irange import irange

# batchmaker()
__batchmaker__regex_pattern__ = r"{(?:[^a-zA-Z0-9{}]+)?([a-zA-Z]|\d+)[^a-zA-Z0-9{}]+([a-zA-Z]|\d+)(?:[^a-zA-Z0-9{}]+(\d+))?(?:[^a-zA-Z0-9{}]+)?}"
__batchmaker__regex_compile__ = re.compile(__batchmaker__regex_pattern__)


def batchmaker(pattern: str):
    """
    Alat Bantu untuk membuat teks yang berulang.
    Gunakan `{[start][separator][finish]([separator][step])}`.
    ```
    [start] dan [finish]    -> bisa berupa huruf maupun angka
    ([separator][step])     -> bersifat optional
    [separator]             -> selain huruf dan angka
    [step]                  -> berupa angka positif
    ```

    ```python
    s = "Urutan {1/6/3} dan {10:9} dan {j k} dan {Z - A - 15} saja."
    print(batchmaker(s))
    print(list(batchmaker(s)))
    ```
    """
    s = __batchmaker__regex_compile__.search(pattern)
    if s is None:
        yield pattern
        return

    find = s.group()
    start, finish, step = s.groups()

    for i in irange(start, finish, step):
        r = pattern.replace(find, i, 1)
        yield from batchmaker(r)


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv
    from ..ifunctions.iprint import iprint

    if i := iargv(1):
        iprint(batchmaker(i))

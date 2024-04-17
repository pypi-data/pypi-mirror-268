from ..ibuiltins.is_empty import is_empty


def irange(start, finish, step=1):
    """
    Meningkatkan fungsi range() dari python untuk pengulangan menggunakan huruf

    ```python
    print(irange('a', 'c'))
    print(irange('z', 'a', 10))
    print(list(irange('a', 'z', 10)))
    print(list(irange(1, '7')))
    print(list(irange(10, 5)))
    ```
    """

    def casting_class():
        start_int = isinstance(start, int)
        finish_int = isinstance(finish, int)
        start_str = isinstance(start, str)
        finish_str = isinstance(finish, str)
        start_numeric = start.isnumeric() if start_str else False
        finish_numeric = finish.isnumeric() if finish_str else False

        if start_numeric and finish_numeric:
            # irange("1", "5")
            return (int, str)

        if (start_numeric or start_int) and (finish_numeric or finish_int):
            # irange("1", "5")
            # irange("1", 5)
            # irange(1, "5")
            # irange(1, 5)
            return (int, int)

        if start_str and finish_str:
            # irange("a", "z")
            # irange("p", "g")
            return (ord, chr)

        """
        kedua if dibawah ini sudah bisa berjalan secara logika, tetapi
        perlu dimanipulasi supaya variabel start dan finish bisa diubah.
        """
        # irange(1, 'a') -> irange('1', 'a')
        # irange(1, '5') -> irange(1, 5)
        # irange('1', 5) -> irange(1, 5)
        # irange('a', 5) -> irange('a', '5')
        #
        # if start_str and finish_int:
        #     # irange("a", 5) -> irange("a", "5")
        #     finish = str(finish)
        #     return (ord, chr)
        #
        # if start_int and finish_str:
        #     # irange(1, "g") -> irange("1", "g")
        #     start = str(start)
        #     return (ord, chr)

        raise Exception(f"[{start} - {finish}] tidak dapat diidentifikasi kesamaannya")

    counter_class, converter_class = casting_class()
    start = counter_class(start)
    finish = counter_class(finish)

    step = 1 if is_empty(step) else int(step)

    faktor = 1 if finish > start else -1
    step *= faktor
    finish += faktor

    for i in range(start, finish, step):
        yield converter_class(i)


if __name__ == "__main__":
    from .iargv import iargv
    from .iprint import iprint

    if (s := iargv(1)) and (f := iargv(2)):
        iprint(irange(s, t))

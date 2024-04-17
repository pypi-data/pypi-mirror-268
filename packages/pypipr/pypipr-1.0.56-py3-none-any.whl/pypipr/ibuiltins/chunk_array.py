def chunk_array(array, size, start=0):
    """
    Membagi array menjadi potongan-potongan dengan besaran yg diinginkan

    ```python
    array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]
    print(chunck_array(array, 5))
    print(list(chunck_array(array, 5)))
    ```
    """
    for i in range(start, len(array), size):
        yield array[i : i + size]

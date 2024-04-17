def print_to_last_line(text: str):
    """
    Melakukan print ke konsol tetapi akan menimpa baris terakhir.
    Berguna untuk memberikan progress secara interaktif.

    ```python
    c = input("masukkan apa saja : ")
    print_to_last_line(f"masukkan apa saja : {c} [ok]")
    ```
    """
    print(f"\033[F{text}")

import random
import string


def password_generator(
    length=8, characters=string.ascii_letters + string.digits + string.punctuation
):
    """
    Membuat pssword secara acak

    ```python
    print(password_generator())
    ```
    """

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


if __name__ == "__main__":
    from ..ifunctions.iargv import iargv

    length = iargv(1, int, 8)
    print(password_generator(length))

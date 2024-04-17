import platform

LINUX = platform.system() == "Linux"


if __name__ == "__main__":
    print(LINUX)

import platform

WINDOWS = platform.system() == "Windows"

if __name__ == "__main__":
    print(WINDOWS)

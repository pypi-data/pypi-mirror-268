import os

def main():
    """
    Program utama
    """

    # Ambil folder dari file script
    script_folder = os.path.dirname(os.path.realpath(__file__))

    # Ambil semua file Python di dalam folder dan subfolder secara recursive
    files = [
        os.path.join(dirpath, filename)
        for dirpath, dirnames, filenames in os.walk(script_folder)
        for filename in filenames
        if filename.endswith(".py") and filename != "__init__.py"
    ]

    # Urutkan daftar file berdasarkan nama file
    files.sort(key=lambda x: os.path.basename(x))

    # Print semua nama file dengan nomor urut
    for i, file in enumerate(files):
        filename = os.path.splitext(os.path.basename(file))[0]
        print(f"{i}. {filename}")

    # Minta input user berupa angka
    input_user = int(input("Pilih file Python yang ingin dijalankan (0-N): "))

    # Jalankan file Python yang dipilih
    filename = files[input_user]
    os.system(f"python {os.path.abspath(filename)}")

if __name__ == "__main__":
    main()


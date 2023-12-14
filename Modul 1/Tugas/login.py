def login():
    while True:
        print("\nSelamat datang di Perpustakaan!")
        peran = input("Login sebagai : \n1. admin\n2. user\npilih :\n")

        if peran not in ["admin", "user"]:
            print("Peran tidak valid. Silakan masukkan 'admin' atau 'user'.")
            continue
        return peran
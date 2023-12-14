import login
daftar_buku = []
def tampilkan_daftar_buku():
    print("\nDaftar Buku Saat Ini:")
    for index, buku in enumerate(daftar_buku, start=1):
        status = "Tersedia" if buku['tersedia'] else "Dipinjam"
        print(f"{index}. {buku['judul']} - {status}")

def tambah_buku(judul):
    buku_baru = {'judul': judul, 'tersedia': True}
    daftar_buku.append(buku_baru)
    print(f"Buku '{judul}' telah ditambahkan ke perpustakaan.")

def pinjam_buku(index):
    if 1 <= index <= len (daftar_buku):
        buku = daftar_buku[index - 1]
        if buku['tersedia']:
            buku['tersedia'] = False
            print(f"Anda telah meminjam buku '{buku['judul']}'")
        else:
            print(f"Buku '{buku['judul']}' sudah dipinjam lur.")
    else:
        print(f"Pilihan tidak ada.")
            
def kembalikan_buku(index):
    if 1 <= index <= len(daftar_buku):
        buku = daftar_buku[index - 1]
        if buku['tersedia']:
            print(f"Anda belum meminjam '{buku['judul']}' ini lur hmm.")
        else:
            buku['tersedia'] = True
            print(f"Anda telah mengembalikan buku '{buku['judul']}'.\n TERIMAKASIH dan silahkan pinjam kembali")
    else:
        print("Indeks buku tidak valid.")
while True:
    peran = login.login()
    while True:
        print("\nMenu:")
        print("1. Lihat Daftar Buku")
        if peran == "admin":
            print("2. Tambah Buku")
        elif peran == "user":
            print("2. Pinjam Buku")
            print("3. Kembalikan Buku")
        print("0. Keluar")

        pilihan = input("Pilih : ")

        if pilihan == "0":
            break
        elif pilihan == "1":
            tampilkan_daftar_buku()
        elif pilihan == "2" and peran == "admin":
            judul = input("Masukkan judul buku: ")
            tambah_buku(judul)
        elif pilihan == "2" and peran == "user":
            tampilkan_daftar_buku()
            index = int(input("Masukkan nomor buku yang ingin dipinjam: "))
            pinjam_buku(index)  # Meminjam buku
        elif pilihan == "3" and peran == "user":
            tampilkan_daftar_buku()
            index = int(input("Masukkan nomor buku yang ingin dikembalikan: "))
            kembalikan_buku(index)  # Mengembalikan buku
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


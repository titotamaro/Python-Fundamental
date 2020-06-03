barang = []
pilih1 = ""


while pilih1 != "5" :  
    print("===========LIST DATA BARANG===========")
    print("1. Cetak isi daftar barang\n2. Menambahkan data ke daftar barang\n3. Menghapus data dari daftar barang\n4. Mengubah data dalam daftar barang\n5. Exit") 
    print("\n")
    pilih1 = input("Masukkan pilihan angka: ")
### OPSI 1
    if pilih1 == "1" :
        if len(barang) == 0:
            print("Daftar barang masih kosong!")
            print("\n")
        else:
            print("======DAFTAR BARANG======")
            for i in range (0,len(barang)):
                 print(f"{i+1}. {barang[i]}")
            print("\n")
### OPSI 2
    elif pilih1 == "2":
        tambah_data = input("Masukkan data barang yang akan diinput: ")
        lower_tambah_data = tambah_data.lower()
        split_input = lower_tambah_data.split(", ")
        for i in split_input:
            try:
                int(i)
                print(f"Data '{i}' yang anda akan masukkan salah!")
                print("\n")
            except:
                if i in barang:
                    YorN = ""
                    opsi = ["Y","N"]
                    while YorN == "Y" or "N":
                        YorN = input(f"Data '{i}' sudah ada sebelumnya, apakah tetap akan disimpan (Y/N)?")
                        if YorN.upper() == "Y":
                            barang.append(i)
                            print(f"Data '{i}' tersimpan")
                            print("\n")
                            break
                        elif YorN.upper() == "N":
                            print(f"Data '{i}' tidak tersimpan")
                            print("\n")
                            break
                        else :
                            print("Pilihan opsi salah, mohon pilih opsi yang benar!")
                else:
                    barang.append(i)
                    print(f"Data '{i}' tersimpan")
                    print("\n")
### OPSI 3
    elif pilih1 == "3":
        hapus = input("Masukkan data barang yang akan dihapus: ")
        lower_hapus = hapus.lower()
        if lower_hapus not in barang:
            print(f"Nama barang '{lower_hapus}' tidak tersedia")
            print("\n")
        else:
            for i in range(0,barang.count(lower_hapus)):
                barang.remove(lower_hapus)
            print(f"Data '{lower_hapus}' telah terhapus!")
            print("\n")
### OPSI 4
    elif pilih1 == "4":
        ubah = input("Masukkan data barang yang akan diubah: ")
        lower_ubah = ubah.lower()
        if lower_ubah not in barang:
            print(f"Nama barang '{lower_ubah}' tidak tersedia!")
            print("\n")
        else:
            ubah1 = input("Masukkan perubahan data: ")
            lower_ubah1 = ubah1.lower()
            for i in range (0,len(barang)):
                if barang[i] == lower_ubah:
                    barang[i] = lower_ubah1
            print("Data terupdate!")
            print("\n")
### OPSI 5
    elif pilih1 == "5":
        print("Anda Telah Keluar Dari Aplikasi!")
### INPUT SALAH
    else:
        print("Pilihan anda tidak ada dalam opsi, mohon masukkan pilihan yang benar!")
        print("\n")


barang = {}
pilih1 = ""


while pilih1 != "5" :  
    print("===========LIST DATA BARANG===========")
    print("1. Cetak isi daftar barang\n2. Menambahkan data ke daftar barang\n3. Menghapus data dari daftar barang\n4. Mengubah jumlah data dalam daftar barang\n5. Exit") 
    print("\n")
    pilih1 = input("Masukkan pilihan angka: ")
### OPSI 1
    if pilih1 == "1" :
        if len(barang) == 0:
            print("Daftar barang masih kosong!")
            print("\n")
        else:
            print("======DAFTAR BARANG======")
            for item in barang:
                 print(item,":", barang[item])
            print("\n")
### OPSI 2
    elif pilih1 == "2":
        item = input("Masukkan nama barang: ")
        item = item.lower()
        ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'item' (tidak bolah hanya angka)
        try :
            int(item)
            print(f"Data yang anda akan masukkan salah!")
            print("\n")
        except :
             ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'quantity' (tidak boleh string)
            try :
                quantity = int(input("Masukkan jumlah barang: "))  
                if item in barang:
                    YorN = input("Data barang sudah tersedia, apakah jumlah barang akan ditambahkan (Y/N)?")
                    if YorN.upper() == "Y":
                        barang[item] += quantity
                        print("Data berhasil dimasukkan")
                        print("\n")
                    elif YorN.upper() == "N":
                        print("Data tidak dimasukkan")
                        print("\n")
                    else :
                        print("Pilihan opsi salah, mohon ulang kembali!")    
                        print("\n")
                else :
                    barang[item] = quantity
                    print("Data berhasil dimasukkan")
                    print("\n")
            except :
                print(f"Data yang anda akan masukkan salah!")
                print("\n")
### OPSI 3
    elif pilih1 == "3":
        item = input("Masukkan data barang yang akan dihapus: ")
        item = item.lower()
        if item not in barang:
            print("Data barang tidak ditemukan!")
            print("\n")
        else:
            del(barang[item])
            print("Data berhasil dihapus!")
            print("\n")  
### OPSI 4
    elif pilih1 == "4":
        item = input("Masukkan data barang yang akan diubah: ")
        item = item.lower()  
        if item not in barang:
            print("Nama barang tidak tersedia!")
            print("\n")
        else:
            ## try, except ini untuk pengecekan benar tidaknya jenis data pada input 'quantity' (tidak boleh string)
            try:
                quantity = int(input("Masukkan perubahan jumlah data: "))
                barang[item]=quantity
                print("Data terupdate!")
                print("\n")
            except:
                print("Format yang anda masukkan salah!")
### OPSI 5
    elif pilih1 == "5":
        print("Anda Telah Keluar Dari Aplikasi!")
### INPUT SALAH
    else:
        print("Pilihan anda tidak ada dalam opsi, mohon masukkan pilihan yang benar!")
        print("\n")


barang = {}
pilih1 = ""


while pilih1 != "5" :  
    print("===========LIST DATA BARANG===========")
    print("1. Cetak isi daftar barang\n2. Menambahkan data ke daftar barang\n3. Menghapus data dari daftar barang\n4. Mengubah data dalam daftar barang\n5. Exit") 
    print("\n")
    pilih1 = input("Masukkan pilihan angka: ")
## OPSI 1
    if pilih1 == "1" :
        if len(barang) == 0:
            print("Daftar barang masih kosong!")
            print("\n")
        else:
            print("=NAMA BARANG=||=JUMLAH=")
            print("")
            for item in sorted(barang, key=barang.get, reverse=False):
              print(item,":",barang[item])
            print("")  
## OPSI 2
    elif pilih1 =="2":
     item = input("Masukkan nama barang: ")
     quantity = int(input("Masukkan jumlah barang: "))  
     barang[item] =+ quantity
     if item == barang[item]:
         YorN = input("Data barang yang sama terdeteksi, apakah barang tetap disimpan (Y/N)?")
         if YorN == "y" or "Y":
             barang[item] =+ quantity
             print("Data berhasil dimasukkan")
         elif YorN == "n" or "N":
             print("Data tidak dimasukkan")    
### OPSI 3
    elif pilih1 == "3":
        item = input("Masukkan data barang yang akan dihapus: ")
        item = item.lower()
        if item not in barang:
            print("Data barang tidak ditemukan!")
            print("\n")
        else:
            del(barang[item])
            print("Data berhasil dihapus")
            print("")    
### OPSI 4
    elif pilih1 == "4":
        item = input("Masukkan data barang yang akan diubah: ")
        item = item.lower()  
        if item not in barang:
            print(f"Nama barang '{item}' tidak tersedia!")
            print("\n")
        else:
            item = input("Masukkan perubahan data: ")
            quantity = int(input("Masukkan perubahan jumlah data: "))
            barang[item]=quantity
            print("Data terupdate!")
            print("\n")
### OPSI 5
    elif pilih1 == "5":
        print("Anda Telah Keluar Dari Aplikasi!")
### INPUT SALAH
    else:
        print("Pilihan anda tidak ada dalam opsi, mohon masukkan pilihan yang benar!")
        print("\n")


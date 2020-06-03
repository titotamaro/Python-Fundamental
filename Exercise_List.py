# Soal 1

# Input : Nama hari dan tidak case sensitive
# Jumlah : dalam integer
# Pengecekan : "Tidak ada nama hari" # Jika input tidak sesuai
# Output : jumlah hari ke depan adalah hari apa? 

# ANSWER

# hari_sekarang     = input("Nama hari saat ini (untuk hari ke 5 gunakan jum'at bukan jumat): ")
# jumlah            = int(input("Jumlah hari kedepan / kebelakang: "))
# hari              = ["senin", "selasa", "rabu", "kamis", "jum'at", "sabtu", "minggu"]
# hari_sekarang     = hari_sekarang.lower()

# if hari_sekarang == hari[0] :
#     hari_sekarang = 1
# elif hari_sekarang == hari[1] :
#     hari_sekarang = 2
# elif hari_sekarang == hari[2] :
#     hari_sekarang = 3
# elif hari_sekarang == hari[3] :
#     hari_sekarang = 4
# elif hari_sekarang == hari[4] :
#     hari_sekarang = 5
# elif hari_sekarang == hari[5] :
#     hari_sekarang = 6
# elif hari_sekarang == hari [6] :
#     hari_sekarang = 7 
# else :
#     print ("Tidak ada nama hari")

# jumlah2 = (hari_sekarang + jumlah)% 7    

# if jumlah2 == 0 :
#     hari_baru = "minggu"
# elif jumlah2 == 1 :
#     hari_baru = "senin"    
# elif jumlah2 == 2 :
#     hari_baru = "selasa"
# elif jumlah2 == 3 :
#     hari_baru = "rabu"
# elif jumlah2 == 4 :
#     hari_baru = "kamis"
# elif jumlah2 == 5 :
#     hari_baru = "jum'at" 
# else:
#     hari_ini = "sabtu"

# print (f"Nama hari dalam {jumlah} hari dari sekarang adalah hari {hari_baru}")    


# Soal 2

# Palindrome
# input = masukkan kata
# output = kata tersebut palindrome atau tidak

# ANSWER :

# kata = input("Masukkan kata yang akan dicek: ")

# kata2 = list(kata)

# kata_balik = kata2 [::-1]

# if kata2 == kata_balik:
#     print (f"Kata {kata} merupakan palindrome")
# else :
#     print (f"Kata {kata} bukan merupakan palindrome")    


# Soal 3
# Masukkan kalimat : Hari ini hari selasa
# Ada 2 pilihan (opsi 1 dan opsi 2)
# Opsi 1 :
# Masukkan karakter : a
# Output : Hri ini hri sls
# Opsi 2 :
# Masukkan karakter vokal
# Output : Horo ono horo soloso

# ANSWER

# kalimat     = input("Masukkan kalimat: ")
# karakter    = input("Masukkan karakter: ")
# opsi        = int(input("Masukkan angka 1 atau angka 2: "))

# if opsi == 1 :
#     hasil = kalimat.replace(karakter,'')
#     print(f"Kalimat menjadi: {hasil}")

# elif opsi == 2 :
#     hasil1 = kalimat.replace('a', '~')
#     hasil2 = hasil1.replace('i', '~')
#     hasil3 = hasil2.replace('u', '~')
#     hasil4 = hasil3.replace('e', '~')
#     hasil5 = hasil4.replace('o', '~')
#     hasil  = hasil5.replace('~',karakter)
#     print(f"Kalimat menjadi: {hasil}")

# else :
#     print("Opsi tidak valid")    


# Soal 4 (gunakan try dan except di soal nomor 4 dan 5) , gunakan juga numerical methode
# Input : masukkan  4 digit angka = 5689
# Output : 8956
# Error handling : Angka yang anda masukkan salah

# ANSWER

# angka = int(input("Masukkan 4 digit angka: ")) 

# if 999 < angka < 9999 :
#     a = angka // 1000
#     sisa_a = angka % 1000
#     b = sisa_a // 100
#     sisa_b = sisa_a % 100
#     c = sisa_b // 10
#     sisa_c = sisa_b % 10
#     d = sisa_c // 1

#     print (c,d,a,b)

# else:
#     print("Angka yang anda masukkan tidak valid")

# Soal 5
# Input : Masukkan angka 2 digit = 85
# Masukkan 2 digit kedua = 32
# Output 8532

# ANSWER

# angka1 = int(input("Masukkan 2 digit pertama angka yang diinginkan: "))
# angka2 = int(input("Masukkan 2 digit akhir angka yang diinginkan: "))

# if angka1 <=99 and angka2 <=99 :
#     a = angka1 * 100
#     b = angka2 * 1
#     c = a+b

#     print(c)
# else :
#     print("Angka yang anda masukkan tidak valid")

#ada try and catch saat olah database (modul2) --> untuk pengganti try and except 
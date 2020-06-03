# Latihan :
# User dapat memasukkan huruf kapital/ kecil
# Pilihan translate 1. IDN-ENG, 2. ENG-IDN
# Pilih 1 :
# Masukkan nama hari 
# Kondisi : nama hari yang anda masukkan salah
# Output : Nama hari ... dalam bahasa inggris adalah ...
# Pilih 2 :
# Sama tapi bahasa inggris

hari = {"senin":"monday",
        "selasa":"tuesday",
        "rabu":"wednesday",
        "kamis":"thursday",
        "jumat":"friday",
        "sabtu":"saturday",
        "minggu":"sunday" 
        }
        
day1 = {}
pilih=""

for i, j in hari.items():
    day1[j]=i 

while pilih != "3" :
    print("")
    print("++++++++++TRANSLATOR++++++++++")
    print("")
    print("1. Terjemahan IDN-ENG\n2. Terjemahan ENG-IDN\n3. Exit " )
    print("")
    pilih =  input("Masukkan opsi: ")
### Opsi 1
    if pilih == "1":
        namahari = input("Masukkan nama hari(IDN): ")
        namahari.lower()
        if namahari in hari:
            print(f"Nama hari {namahari} dalam bahasa inggris adalah {hari[namahari]} ")
        else:
            print("Nama hari yang anda masukkan salah!") 
### Opsi 2
    elif pilih == "2" :
        day = input("Enter the name of day(ENG): ")
        day.lower()
        if day in day1:  
            print(f"The name of day {day} in Indonesian is {day1[day]}")
        else:
            print("Nama hari yang anda masukkan salah!")    
### Opsi 3
    elif pilih == "3" :
        print("\nAnda telah keluar, terimakasih!\n")      
    else:
        print("Pilihan yang anda masukkan salah!")                   

         
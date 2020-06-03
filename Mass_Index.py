# Exercise 1
# Input : Masukkan nilai
# NILAI PALING atas 100 dan paling bawah 0

# kondisi :
# nilai diatas 100 :
# NILAI diluar jangkauan
# nilai dibawah 0:
# Tidak bisa menerima nilai negatif

# Kondisi :
# 90 keatas grade A
# 85 keatas grade A-
# 80 keatas grade B
# 75 keatas grade B-
# 70 keatas grade C
# 65 keatas grade D
# di bawah itu REMIDIAL

# OUTPUT : 
# Nilai anda (nilai) dan Grade anda (grade)

# Answer 1

nilai = int(input("Masukkan nilai anda: "))

if nilai > 100 :
    print("Nilai diluar jangkauan")
elif nilai >= 90 :
    print(f"Nilai anda {nilai} dan Grade anda A")
elif nilai >= 85 :
    print(f"Nilai anda {nilai} dan Grade anda A-")
elif nilai >=80 :
    print(f"Nilai anda {nilai} dan Grade anda B")
elif nilai >=75 :
    print(f"Nilai anda {nilai} dan Grade anda B-")
elif nilai >=70 :
    print(f"Nilai anda{nilai} dan Grade anda C")
elif nilai >=65 :
    print(f"Nilai anda {nilai} dan Grade anda D")
elif nilai < 0 :
    print("Tidak bisa menerima nilai negatif")
else:
    print ("Anda Remedial")        

# Exercise 2 :
# input : masukkan angka
# Kondisi : cek angka
# Output : angka yang anda masukkan (angka) adalah angka GENAP / GANJIL

# Answer 2

angka = int(input("Masukkan Angka: "))
cek = angka % 2

if cek == 0 :
    print(f"Angka yang anda masukkan {angka} adalah angka Genap")
else:
    print(f"Angka yang anda masukkan {angka} adalah angka Ganjil")    

# Exercise 3 :
# rumus : IMT = massa (kg) / tinggi (m) ^ 2

# input : 
# masukkan Massa (Kg)
# masukkan tinggi (cm)

# Kondisi :
#  IMT < 18.5 = berat badan kurang
#  18.5 - 24.9 = berat badan ideal
#  25 - 29.9 = berat badan berlebih
#  30 - 39.9 = BB sangat berlebih 
#  IMT > 39.9 = obesitas

#  Output :
#  Massa : (massa) (Kg)
# Tinggi : (tinggi) (m) 
# IMT ....., BERAT BADAN ANDA IDEAL (sesuai kondisi)

# Answer 3

massa = int(input("Masukkan massa anda (kg): "))
tinggi = int(input("Masukkan tinggi anda (cm):  "))

imt = round(massa / (tinggi/100)**2,2)

if imt < 18.5 :
    print(f"IMT anda adalah {imt}, Berat Badan Kurang")
elif imt <= 24.9 :
    print(f"IMT anda adalah{imt}, Berat Badan Ideal")   
elif imt <=29.9 :
    print(f"IMT anda adalah{imt}, Berat Badan Berlebih")
elif imt <=39.9 :
    print(f"IMT anda adalah {imt}, BB sangat berlebih")
else :
    print(f"IMT anda adalah {imt}, Obesitas")             
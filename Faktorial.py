import math

angka = int(input("Masukkan jumlah iterasi faktorial yang Anda inginkan: "))

def Faktorial(x):
    if x <= 0:
        return "Angka tidak Valid, mohon coba kembali"
    else:
        return math.factorial(x)

print(f"Faktorial dari {angka} adalah {Faktorial(angka)}")
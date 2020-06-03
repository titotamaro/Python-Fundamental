def Kalkulator(x,y,z):
    if z == '+':
        return x+y
    elif z == '-': 
        return x-y   
    elif z == '/':
        return x/y
    elif z == '*':
        return x*y


angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
operator = input("Masukkan operasi yang diinginkan (+) (-) (/) (*): ")
print (f"Angka Hasil Operasi adalah : {Kalkulator(angka1,angka2,operator)}")



    



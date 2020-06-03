def AngkaKeRomawi(y): # tidak menggunakan x agar tidak tertuka dengan "X" roman numerals
    if not 0 < y < 4000:
        print("Error! Value tidak boleh dibawah 0 atau diatas 4000")
    nilai = (1000,900,500,400,100,90,50,40,10,9,5,4,1) # 13 item
    huruf = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I") # 13 item 
    hasil = []
    for i in range(len(nilai)):
        hitung = int(y/nilai[i]) # Jumlah konversi per huruf: misal M = 3 atau X = 2 ## sama dengan menggunakan %
        hasil.append(huruf[i]*hitung)
        y -= nilai[i]*hitung 
    return ''.join(hasil)     


def RomawiKeAngka(y): 
    y = y.upper()
    roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    total = 0            
    for i in range (len(y)):
        try:
            value = roman[y[i]]
            if i+1 < len(y) and roman[y[i+1]]>value: # bilangan di sebelah kanan lebih besar dari bilangan sebelah kiri dan sampai digit kedua sebelum terakhir
                total-=value
            else:
                total+= value
        except:
            print("Input tidak Valid")
    if AngkaKeRomawi(total) == y: # pengecekan menggunakan fungsi sebelumnya
        return total
    else:
        print("Input angka Romawi tidak valid")  

user_input = input("Masukkan angka romawi atau angka biasa: ")
if user_input.isalpha() == False:
    user_input = int(user_input)
    print(AngkaKeRomawi(user_input))
else:
    print(RomawiKeAngka(user_input))  


def CaesarCipher(x,y): # x = kalimat ; y = step / langkah
    if x.isdigit == True:
        print("Caesar Cipher tidak bisa digunakan untuk data tipe Integer")
    else:    
        x.lower()
        alphabet = 'abcdefghijklmnopqrstyvwxyz'
        hasil = ""
        for i in x:  
            if i == " ":
                hasil+=i
            else:
                lokasi = alphabet.find(i)
                lokasi_new = (lokasi + y) % 26 # yang ke 27 = a
                hasil += alphabet[lokasi_new] 
    return hasil   

z = input("Masukkan kata: ")
v = int(input("Masukkan nilai geser karakter: "))
print(CaesarCipher(z,v))


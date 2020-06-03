# Latihan
# input : masukkan kalimat

# outputnya : kata dalam kalimat dibalik

# input : " nama saya joni"
# output: "aman ayas inoj"

## Answer ##

kalimat = input("Masukkan kalimat yang akan dibalik: ") # string
kata = kalimat.split() # menjadi list dan terpisah dimana kata[0] = kata pertama

for i in range (0, len(kata)): # iterasi dilakukan sebanyak jumlah kata
    print (kata[i][::-1], end=" ") # setiap kata dibalik perindexnya dan nonaktivasi "\n" pada fungsi print      

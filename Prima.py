import math

x = int(input("Angka yang ingin dicek: "))

y = x%2
z = x%3

if y == 0 :
    print("Angka ini merupakan angka genap")
elif y != 0  :
    print ("Angka ini merupakan angka ganjil")
elif y != 0 and z != 0 :
    print ("Angka ini merupakan angka ganjil dan angka prima")
else :
    print ("Angka ini merupakan angka ganjil dan angka prima")    
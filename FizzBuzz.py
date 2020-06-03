def FizzBuzz (x,y):
    for i in range(x,y+1):
        if i%3 == 0 and i%5 == 0:
            print ("FizzBuzz")
        elif i%3 == 0:
            print ("Fizz")
        elif i%5 == 0 :
            print ("Buzz")
        else:
            print (i)

angka1 = int(input("Masukkan Angka Awal Iterasi: "))  
angka2 = int(input("Masukkan Angka Akhir Iterasi: "))
FizzBuzz(angka1,angka2)



 
        

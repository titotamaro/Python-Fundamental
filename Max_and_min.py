import random

mylist=[] # Generate random number on the list
x = int(input("Masukkan jumlah data yang akan diiterasi: "))
for i in range(x):
    mylist.append(random.randrange(1,200))

def maxima(list_a):
    indexing_length = len(list_a)-1 #[1,2,3,4,5==> tdk bisa dibandingkan karena paling kanan]
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i]>list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #swapping location based on value

    return list_a[-1]           

print((mylist),"==> Belum Sort")
print(maxima(mylist),"==> Menggunakan Maxima")  

def minima(list_b):
    indexing_length = len(list_b)-1 #[1,2,3,4,5==> tdk bisa dibandingkan karena paling kanan]
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_b[i]>list_b[i+1]:
                sorted = False
                list_b[i], list_b[i+1] = list_b[i+1], list_b[i] #swapping location based on value

    return list_b[0]

print(minima(mylist)," ==> Menggunakan Minima")    
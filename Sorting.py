import random

#Bubble Sort
mylist=[] # Generate random number on the list
x = int(input("Masukkan jumlah data yang akan diiterasi: "))
for i in range(x):
    mylist.append(random.randrange(1,200))

def bubble_ascending(list_a):
    indexing_length = len(list_a)-1 #[1,2,3,4,5==> tdk bisa dibandingkan karena paling kanan]
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_a[i]>list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #swapping location based on value
    return list_a            

print(mylist, "==> Sebelum Sort")       
print(bubble_ascending(mylist), "==> Setelah Sort Ascending")

def bubble_descending(list_b):
    indexing_length = len(list_b)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list_b[i]<list_b[i+1]:
                sorted = False
                list_b[i], list_b[i+1] = list_b[i+1], list_b[i]
    return list_b            
     
print(bubble_descending(mylist), "==> Setelah Sort Descending")





       

            




import random
import math

# Bubble Sort
mylist=[] # Generate random number on the list
x = int(input("Masukkan jumlah data yang akan diiterasi: "))
for i in range(x):
    mylist.append(random.randrange(1,1000))

print(mylist)
print("")

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

# Modus ==> Nilai yang paling sering muncul
def modus (list_b):
    angka = (0,0)
    for i in list_b:
        muncul = list_b.count(i)
        if muncul > angka[0]:
            angka = (muncul, i)
    return angka[1]

print(modus(mylist),"  ==> Modus Data")            

#Mean ==> Rata-rata nilai data
def mean (list_c):
    total = 0 #storage
    for i in list_c:
        total += i
    return round(total/len(list_c),2) # pembulatan 2 angka dibelakang koma   

print(mean(mylist),"==> Mean Data")

#Median / Quartil 2 ==> Nilai tengah setelah data diurutkan
def quartil2 (list_d):
    bubble_ascending(list_d)
    if len(list_d) / 2 != 0:
        middle_index = (len(list_d)/2)    # jumlah data dibagi 2 , menggunakan int agar hasil tidak decimal
        pembulatan = math.ceil(middle_index) # pembulatan ke atas
        return list_d[pembulatan]
    elif len(list_d) / 2  == 0:
        middle_index_1 = (len(list_d)/2)        # middle index 1
        middle_index_2 = (len(list_d)/2) - 1    # middle index 2
        return (list_d[middle_index_1] + list_d[middle_index_2]) / 2 # ditambah dan bagi 2 / rata- rata
    else:
        print ("ERROR!")    

print(quartil2(mylist),"  ==> Median / Quartil 2")

# Quartil 1
def quartil1 (list_e):
    bubble_ascending(list_e) # sorting dan nilai median
    if len(list_e) / 2 == 0:
        middle_index = (len(list_e)/2)    
        pembulatan = math.ceil(middle_index) 
        list25 = list_e[0:pembulatan+1] # slicing list 25%
        index_quartil1 = len(list25) / 2 # jika jumlah data genap, maka list25%  ganjil 
        pembulatan2 = math.ceil(index_quartil1)
        return list_e[pembulatan2]
    elif len(list_e) / 2  != 0:
        middle_index = (len(list_e)/2)    
        pembulatan = math.ceil(middle_index)
        list25 = list_e[0:pembulatan+1]
        middle_index1 = int(len(list25)/2)
        middle_index2 = int(len(list25)/2 -1)
        return (list25[middle_index1] + list25[middle_index2])/2
    else:
        print("ERROR!")

print(quartil1(mylist),"==> Quartil 1")       

# Quartil 3
def quartil3 (list_f):
    bubble_ascending(list_f) # sorting dan nilai median
    if len(list_f) / 2 == 0:
        middle_index = (len(list_f)/2)    
        pembulatan = math.ceil(middle_index) 
        list75 = list_f[pembulatan:] # slicing list 75%
        index_quartil3 = len(list75) / 2 # jika jumlah data genap, maka list75%  ganjil 
        pembulatan2 = math.ceil(index_quartil3)
        return list75[pembulatan2]
    elif len(list_f) / 2  != 0:
        middle_index = (len(list_f)/2)    
        pembulatan = math.ceil(middle_index)
        list75 = list_f[pembulatan:] # slicing list 75%
        middle_index1 = int(len(list75)/2)
        middle_index2 = int(len(list75)/2 -1)
        return (list75[middle_index1] + list75[middle_index2])/2
    else:
        print("ERROR!")

print(quartil3(mylist),"==> Quartil 3")  

# Outlier

def outlier(list_g):
    bubble_ascending(list_g)
    IQR = quartil3(list_g) - quartil1(list_g)
    Lower_Outlier = quartil1(list_g) - (1.5 * IQR)
    Upper_Outlier = quartil3(list_g) + (1.5 * IQR)

    for i in list_g:
        if i < Lower_Outlier:
            return i
        elif i > Upper_Outlier:
            return i 
        else:
            pass
                
print(outlier(mylist), " ==> Outlier")




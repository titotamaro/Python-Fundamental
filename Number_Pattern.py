# lat 1 :
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

## Answer-1 ##

# lower = 1 # angka paling kecil
# upper = 5 # angka paling besar

# print("="*100,end="") # pembatas
# for baris in range(upper+1): 
#     for kolom in range (baris):
#         print(baris, end="") # (end = "") meniadakan "\n" pada fungsi print
#     print("") # setiap loop pada "kolom" di munculkan dalam baris baru              
# print("="*100) # pembatas

# cara 2 and mirror 

# for i in range (1,6):
#     print("  "*(6-i)+(str(i)+" ")*i)

# # Lat 2 :
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4 
# # 1 2 3 4 5

# ## Answer-2 ##

# print("="*100) # pembatas
# for baris in range(upper+1):
#     for kolom in range (lower,baris+1):
#         print(kolom, end="")
#     print("")    
# print("="*100) # pembatas

# # # Lat 3 :
# # # 5
# # # 5 4
# # # 5 4 3 
# # # 5 4 3 2 
# # # 5 4 3 2 1 

# ## Answer-3 ##

# print("="*100) # pembatas
# for baris in range(lower,upper+1):
#     for kolom in range (upper,baris-1,-1):
#         print(kolom, end="")
#     print("")
# print("="*100) # pembatas 

# # #  Lat 4 : 
# # # 1 1 1 1 1
# # # 2 2 2 2
# # # 3 3 3
# # # 4 4 
# # # 5

# ## Answer-4##

# print("="*100) # pembatas
# for baris in range(lower,upper+1):
#     for kolom in range (lower,upper+2-baris):
#         print(baris, end="")
#     print("")
# print("="*100) # pembatas

# # # # Lat 5 :
# # # 1 2 3 4 5 
# # # 1 2 3 4
# # # 1 2 3
# # # 1 2
# # # 1

# ## Answer-5 ##

# print("="*100) # pembatas
# for baris in range(upper,lower-1,-1):
#     for kolom in range (lower,baris+1):
#         print(kolom, end="")
#     print("")
# print("="*100) # pembatas

# # # Lat 6 :
# # # 5 4 3 2 1
# # # 5 4 3 2 
# # # 5 4 3 
# # # 5 4 
# # # 5

# ## Answer-6##

# print("="*100) # pembatas
# for baris in range(upper,lower-1,-1):
#     for kolom in range (baris,lower-1,-1):
#         print(kolom, end="")
#     print("")
# print("="*100) # pembatas    

# # lat 7 :
# #            *
# #          * * * 
# #        * * * * *
# #      * * * * * * *
# #    * * * * * * * * *
# #    * * * * * * * * *
# #      * * * * * * *
# #        * * * * *
# #          * * *
# #            *

# ## Answer-7 ##

# num = 9

# print("="*100) # pembatas
# for i in range(0,num+1):
#     print(" "*(num-i)+"* "*i)
# for i in range(num,0,-1):
#     print(" "*(num-i)+"* "*i)    
# print("="*100) # pembatas

# Lat :
# input : masukkan kalimat

# outputnya : kata dalam kalimat dibalik

# input : " nama saya joni"
# output: "aman ayas inoj"
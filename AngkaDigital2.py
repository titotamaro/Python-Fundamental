# print("====================KONVERSI ANGKA KE ANGKA DIGITAL====================")
# angkadigital =  {1 : {"1" :"    ","2" : " __ ", "3" : " __ ", "4" : "    ", "5" : " __ ", "6" : " __ ", "7" : "__ ", "8" : " __ ", "9" : " __ ", "0" : " __ "},
#         2 : {"1" :"   |", "2" : " __|", "3" : " __|", "4" : "|__|", "5" : "|__ ", "6" : "|__ ", "7" : "  |", "8" : "|__|", "9" : "|__|", "0" : "|  |"},
#         3 : {"1" :"   |", "2" : "|__ ", "3" : " __|", "4" : "   |", "5" : " __|", "6" : "|__|", "7" : "  |", "8" : "|__|", "9" : " __|", "0" : "|__|"}}

# def digital(angka2):
#     hasil = ""
#     for i in range(1,4):
#         for j in angka2:
#             hasil += angkadigital[i][j]
#         hasil += "\n"
#     return hasil

# def digital2(angka2):
#     hasil = ""
#     for i in range(1,4):
#         for j in angka2:
#             hasil += f"{angkadigital[i][j]}" 
#         hasil += "\n"    
#     return hasil       

# inputangka = input("Masukkan angka: ")
# if inputangka.isdigit() == True:
#     print(digital(inputangka))
# else:
#     print("Angka yang anda masukkan salah")
# print("\n")

# print(digital2(inputangka))

# x = [i for i in range(1,11)]
# y = [j for j in range(1,9)]

# print (x)
# print (y)

# for i in x:
#     for j in y:
#         print(i,j)
        
angkadigital =  {1 : {"1" :"    ","2" : " __ ", "3" : " __ ", "4" : "    ", "5" : " __ ", "6" : " __ ", "7" : "__ ", "8" : " __ ", "9" : " __ ", "0" : " __ "},
        2 : {"1" :"   |", "2" : " __|", "3" : " __|", "4" : "|__|", "5" : "|__ ", "6" : "|__ ", "7" : "  |", "8" : "|__|", "9" : "|__|", "0" : "|  |"},
        3 : {"1" :"   |", "2" : "|__ ", "3" : " __|", "4" : "   |", "5" : " __|", "6" : "|__|", "7" : "  |", "8" : "|__|", "9" : " __|", "0" : "|__|"}} 

print(angkadigital[2]["2"])               

# Latihan:
# A = himpunan bilangan genap dari 1 -20
# B = himpunan bilangan ganjil dari 1 -20
# C = himpunan bilangan negatif lebih dari -20
# D = himpunan Bilangan prima dari 1 - 20
# E = himpunan bilangan komposit dari 1 - 20

# Bilangan komposit = Bukan Bilangan prima

# Output :

# a. A ∪ B ∪ C ∪ D ∪ E

# b. (A ∩ B) ∪ (D ∩ E)

# c. (A ∪ B) ∩ (D ∪ E)

# d. (A ∪ B) - (D ∪ E)

# e. (A ∪ B ∪ C) - (A ∩ E)

# # Answer menggunakan bilangan diisi secara manual
# # Catatan : '|' --> Union, '&' --> Intersection, '-' --> Difference, '+' --> Symmetric Difference

a = {2,4,6,8,10,12,14,16,18,20} # Bilangan genap
b = {1,3,5,7,9,11,13,15,17,19} # Bilangan ganjil
c = {-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1} # Bilangan negatif > -20
d = {2,3,5,7,11,13,17,19} # Bilangan prima
e = {4,6,8,9,10,12,14,15,16,18,20} # Bilangan komposit

#Answer a. A ∪ B ∪ C ∪ D ∪ E

u = (a|b|c|d|e)
print(u)

#Answer b. (A ∩ B) ∪ (D ∩ E)

v = ((a&b)|(d&e))
print(v)

#Answer c. (A ∪ B) ∩ (D ∪ E)

w = ((a|b)&(d|e))
print(w)

#Answer d. (A ∪ B) - (D ∪ E)

x = ((a|b)-(d|e))
print(x)

#Answer e. (A ∪ B ∪ C) - (A ∩ E)

y = ((a|b|c)-(a&e))
print(y)

# Answer menggunakan bilangan menggunakan fungsi

# Semesta merupakan bilangan dari -20 sampai 20

# # semesta = {-20,-19,-18,-17,-16,-15,-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

# a = set()
# b = set()
# c = set()
# d = set()
# e = set()

# lower = -20
# upper = 20

# for i in range(lower,upper+1):
#     if i%2 == 0 :
#         a.add(i) # bilangan genap

# for i in range (lower,upper+1) :
#     if i%2 != 0 :
#         b.add(i) # bilangan ganjil

# for i in range(lower,upper+1) :
#     if i<0 :
#         c.add(i) # bilangan negatif > -20

# for num in range(lower,upper+1) :
#     if num > 1 :
#         prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 prime = False
#         if prime:
#             d.add(num) # bilangan prima

# for num in range(lower,upper+1) :
#     if num > 1 :
#         for i in range(2,num):
#             if num%i == 0 :
#                 e.add(num) # bilangan komposit

# #Answer a. A ∪ B ∪ C ∪ D ∪ E

# u = (a|b|c|d|e)
# print(u)

# #Answer b. (A ∩ B) ∪ (D ∩ E)

# v = ((a&b)|(d&e))
# print(v)

# #Answer c. (A ∪ B) ∩ (D ∪ E)

# w = ((a|b)&(d|e))
# print(w)

# #Answer d. (A ∪ B) - (D ∪ E)

# x = ((a|b)-(d|e))
# print(x)

# #Answer e. (A ∪ B ∪ C) - (A ∩ E)

# y = ((a|b|c)-(a&e))
# print(y)
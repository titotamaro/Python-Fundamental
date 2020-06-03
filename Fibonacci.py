from functools import reduce

user_input = int(input("Tentukan banyak deret Fibonacci yang diinginkan: ")) 

def deret_fibo(x):
    w = [0,1]
    for _ in range(2,x):
        w += (reduce(lambda x,y: x+y, w[-2:]),)
    return w[:x]

f = reduce(lambda x,y: x+y , deret_fibo(user_input))    
                                        
print("")
print("===== Deret Fibonacci =====")
print("")
print(deret_fibo(user_input))
print("")
print(f, f" ==> Total Bilangan Fibonacci sampai yang ke-{user_input}")



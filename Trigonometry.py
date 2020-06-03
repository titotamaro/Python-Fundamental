import matplotlib.pyplot as plt
import numpy as np

#Jenis Trigonometri

print("==========Trigonometric Visualization=========")
print("")
print("1. Sin (x)")
print("2. Cos (x)")
print("3. Tan (x)")
print("4. Csc (x)")
print("5. Sec (x)")
print("6. Cot (x)")
print("")
value = input("Masukkan jenis Trigonometri yang akan divisualisasikan (angkanya saja): ")
value_x = float(input("Masukkan nilai x: "))

#Sin
if value == '1':
    x = np.linspace(0, value_x, 1000)
    y = np.sin(x)
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\sin x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Sin from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show()
#Cos
if value == '2':
    x = np.linspace(0, value_x, 1000)
    y = np.cos(x)
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\cos x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Cos from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show()   
#Tan
if value == '3':
    x = np.linspace(0, value_x, 1000)
    y = np.tan(x)
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\tan x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Tan from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show()  
#Csc
if value == '4':
    x = np.linspace(0, value_x, 1000)
    y = 1/(np.sin(x))
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\csc x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Csc from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show() 
#Sec
if value == '5':
    x = np.linspace(0, value_x, 1000)
    y = 1/(np.cos(x))
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\sec x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Sec from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show()    
#Cot
if value == '6':
    x = np.linspace(0, value_x, 1000)
    y = 1/(np.tan(x))
    plt.plot(x, y, linewidth = 3)
    plt.xlabel('x', fontweight = 'bold', fontsize = 12)
    plt.ylabel(r'$\cot x$', fontweight = 'bold', fontsize = 12)
    plt.title(f'Plot of Cot from 0 to {value_x}', fontweight = 'bold', fontsize = 14)
    plt.grid(True)
    plt.show() 




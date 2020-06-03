# For Exit Program
import sys

#Forbidden Character
forbid = ['!','#','$','%','^','&','*','+','<','>','?']

#Input User
email = input("Masukkan Email Anda: ")

#Check Email Format
if "@" and "." not in email:
    print("Format Email yang Anda Masukkan Salah! \n(cek kembali penggunaan .(dot) dan @)")
else:     
    #Email Breakdown
    #Username
    username = email.split("@")
    username = username[0]
    
    #print(username)
 
    #Hosting
    hosting = email.split("@")
    hosting = hosting[1]
    hosting = hosting.split(".")
    hosting = hosting[0]
    
    #print(hosting)

    #Extension
    extension = email.split("@")
    extension = extension[1]
    extension = extension.split(".")
    extension = extension[1]
    
    #print(extension)

    #Checking Email Validation

    
    for i in forbid:
        if i in username:
            print("Format Username yang Anda Masukkan Salah! \n(cek kembali penulisan username Anda)") 
            sys.exit() 
        else:
            continue     
    if username.isdigit() == True:
        print("Format Username yang Anda Masukkan Salah! \n(cek kembali penulisan username Anda)")    
    elif hosting.isnumeric() == True:
        print("Format Hosting yang Anda Masukkan Salah! \n(cek kembali karakter sesudah @)")        
    elif extension.isnumeric() or len(extension) > 5 == True :
        print("Format Extension yang Anda Masukkan Salah! \n(cek kembali extension yang Anda pakai, pastikan dibawah 5 karakter)")
    else:
        print("Email Anda Tervalidasi\nSelamat Datang!")
      
                                 
        

    
            
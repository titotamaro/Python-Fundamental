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
    if username.isalnum == False:
        print("Format Username yang Anda Masukkan Salah! \n(cek kembali penulisan username Anda)")
    else:
        if hosting.isalpha == False:
            print("Format Hosting yang Anda Masukkan Salah! \n(cek kembali karakter sesudah .(dot)")
        else:
            if extension.isalpha and len(extension) <=5 == True:
                print("Format Extension yang Anda Masukkan Salah! \n(cek kembali extension yang Anda pakai, pastikan dibawah 5 karakter")
            else:
                print("Email Anda Tervalidasi\nSelamat Datang!")

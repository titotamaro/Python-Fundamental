def AlphabetToMorse(x):
    morse_code_dictionary = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}                
    x=x.upper()                
    hasil = ""
    for i in x:
        if i != ' ': #spasi
            hasil += morse_code_dictionary[i]+' '
        else:
            hasil += ' ' #spasi
    return hasil
            
def MorseToAlphabet (x):
    morse_code_dictionary = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}  
    x += ' '
    hasil = '' 
    char = '' # per karakter morse code
    for i in x:  
        if (i != ' '): 
            z = 0
            # simpan data per karakter 
            char += i  
        # jika spasi
        else: 
            # z = 1 adalah karakter baru
            z += 1
            # z = adalah kata baru
            if z == 2 : 
                 # menambah spasi
                hasil += ' '
            else: 
                # membalik keys dan value
                hasil += list(morse_code_dictionary.keys())[list(morse_code_dictionary.values()).index(char)] 
                char = '' 
    return hasil            

kalimat = input("Masukkan kata atau kalimat yang akan di-decoding: ")
if '-' not in kalimat:
    print(AlphabetToMorse(kalimat))
else:
    print(MorseToAlphabet(kalimat))    
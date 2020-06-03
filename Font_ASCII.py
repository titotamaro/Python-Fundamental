###STYLE
def style(x):
  if x == 'bold' or '1':
    return '\033[01m'
  elif x == 'underline' or '2':
    return '\033[04m'
  elif x == 'reverse' or '3':
    return '\033[07m'
  elif x == 'strikethrough' or '4':  
    return '\033[09m'
  elif x == 'invisible' or '5':  
    return '\033[08m'
  else:
    return "Style tidak tersedia"  

###FOREGROUND
def fg(x):
  if x == 'black' or '1':
    return '\033[30m'
  elif x == 'red' or '2':
    return '\033[31m'
  elif x == 'green' or '3':
    return '\033[32m' 
  elif x == 'orange' or '4':  
    return '\033[33m'
  elif x == 'blue' or '5':  
    return '\033[34m'
  elif x == 'purple' or '6':
    return '\033[35m'
  elif x == 'cyan'or '7':  
    return '\033[36m'
  elif x == 'lightgrey' or '8':  
    return '\033[37m'
  elif x == 'darkgrey' or '9':
    return '\033[90m'
  elif x == 'lightred' or '10':
    return '\033[91m'
  elif x == 'lightgreen' or '11':  
    return '\033[92m'
  elif x == 'yellow' or '12':
    return '\033[93m'
  elif x == 'lightblue' or '13':  
    return '\033[94m'
  elif x == 'pink' or '14':  
    return '\033[95m'
  elif x == 'lightcyan' or '15':  
    return '\033[96m'
  else: 
    return "Warna Foreground tidak tersedia"  

##BACKGROUND 
def bg (x):
  if x == 'black' or '1':
    return '\033[40m'
  elif x == 'red' or '2':  
    return '\033[41m'
  elif x == 'green' or '3':  
    return '\033[42m'
  elif x == 'orange' or '4':  
    return '\033[43m'
  elif x == 'blue' or '5':  
    return '\033[44m'
  elif x == 'purple' or '6':
    return '\033[45m'
  elif x == 'cyan' or '7':
    return '\033[46m'
  elif x == 'lightgrey' or '8':  
    return '\033[47m'
  else:
    return "Warna Background tidak tersedia"  

##TAMPILAN MENU
print("=========PILIHAN STYLE==========")
print("")
print('1. Bold\n2. Underline\n3. Reverse\n4. Strikethrough\n5. Invisible')
print("")
print("========PILIHAN WARNA TULISAN=========")
print("")
print('1.  Black\n2.  Red\n3.  Green\n4.  Orange\n5.  Blue\n6.  Purple\n7.  Cyan\n8.  Lightgrey\n9.  Darkgrey\n10. Lightred\n11. Lightgreen\n12. Yellow\n13. Lightblue\n14. Pink\n15. Lightcyan')
print("")
print("========PILIHAN WARNA BACKGROUND=========")
print("")
print('1. Black\n2. Red\n3. Green\n4. Orange\n5. Blue\n6. Purple\n7. Cyan\n8. Lightgrey')
print("")

##USER INPUT
user_input_kalimat = input("Masukkan kalimat yang Anda inginkan: ")
user_input_style = input("Masukkan style yang Anda inginkan (misal: bold): ")
user_input_style.lower()
user_input_fg = input("Masukkan warna karakter yang Anda inginkan (misal: red): ")
user_input_fg.lower()
user_input_bg = input("Masukkan warna backgorund yang Anda inginkan (misal:blue): ")
user_input_bg.lower()


##OUTPUT
after_style = style(user_input_style) + user_input_kalimat
after_fg = fg(user_input_fg) + after_style 
after_bg = bg(user_input_bg) + after_fg 

print("")
print(after_bg + '\033[0m')


#Tambahkan ukuran font, style 







user_name=input("Enter username : ")
password=(input("Enter your password : "))
char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"1","2","3","4","5","6","7","8","9","0","@","#","$","%","&","-","+","(",")","*","\"","'",":",";","!","?","_","/",".","~","`","|","•","√","Π","÷","×","×","¶","∆","£","¢","€","¥","^","°","=","{","}","©","®","™","℅","[","]","<",">",","]
#key=""
key=[]
for letter in char:
    if letter in password:
#        key+=letter
        key.append(letter)
#print(key)
print(key)
def crack(password,*args):
    passkey=""
    for letter in password:
        if letter in args:
            passkey+=letter
    return passkey
print(crack(password,*key))
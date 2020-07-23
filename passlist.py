char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"1","2","3","4","5","6","7","8","9","0","@","#","$","%","&","-","+","(",")","*","\"","'",":",";","!","?","_","/",".","~","`","|","•","√","Π","÷","×","×","¶","∆","£","¢","€","¥","^","°","=","{","}","©","®","™","℅","[","]","<",">",","]
password=""
passlist=[]
for i in char[62:120]:
    for j in char:
        for k in char:
            for l in char:
                for m in char[52:62]:
                    for n in char[52:62]:
                        for o in char[52:62]:
                            for p in char[26:52]:
                                guess=p+j+k+l+i+m+n+o
                                passlist.append(guess)
                                print(guess)
print(passlist)                                
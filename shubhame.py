char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',"1","2","3","4","5","6","7","8","9","0","@","#","$","%","&","-","+","(",")","*","\"","'",":",";","!","?","_","/",".","~","`","|","•","√","Π","÷","×","×","¶","∆","£","¢","€","¥","^","°","=","{","}","©","®","™","℅","[","]","<",">",","]
password=""
passlist=[]
for i in char[0]:
    for j in char[0:26]:
        for k in char[62]:
            for l in char[0:26]:
                for m in char[52:62]:
                    for n in char[52:62]:
                        for o in char[52:62]:
                            for p in char[26:52]:
                                guess=p+l+p+l+k+m+n+o
                                passlist.append(guess)
                                print(guess)
print(passlist)         
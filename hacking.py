import hashlib

flag=0

pass_hash = input ("Enter md5 hash: ")
wordlist = input ("File name: ")
try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()
for word in pass_file:
    
    enc_wrd = word.encode( " utf-8")
    digest = hashlib.mds(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("Password found")
        print("pas sword is " + word)
        Flag = 1
        break

if flag == 0:
    Print("Password /nassphrase is not in the 1ist")
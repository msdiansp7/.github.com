for i in range(1,100):    
    n=input(f"{i}).Enter the number : ")
    T1=int(input("From base : "))
    T2=int(input("To base : "))
    if T1==10:
        n4=int(n)
        if T2==2:
            n1=bin(n4)
            print(n1)
        elif T2==8:
            n1=oct(n4)
            print(n1)
        elif T2==16:
            n1=hex(n4)
            print(n1)
        else:
            print("Enter valid base number.")
    elif T1==2:
        dec=0
        n3=str(n)
        n1=list(n3)
        value=0
        l=len(n1)
        for i in range(0,l):
            digit=n1.pop()
            if digit=="1":
                value+=1*pow(2,i)
        dec+=value
        if T2==10:
            print(dec)
        elif T2==8:
            n2=oct(dec)
            print(n2)
        elif T2==16:
            n2=hex(dec)
            print(n2)
        else:
            print("Enter valid number.")
    elif T1==8:
        dec=0
        n3=str(n)
        n1=list(n3)
        value=0
        l=len(n1)
        for i in range(0,l):
            digit=n1.pop()
            if int(digit)!=8 and int(digit)!=9:
                value+=int(digit)*pow(8,i)
                
        dec+=value
        if T2==10:
            print(dec)
        elif T2==2:
            n2=bin(dec)
            print(n2)
        elif T2==16:
            n2=hex(dec)
            print(n2)
        else:
            print("Enter valid number.")
    elif T1==16:
        dec=0
        n3=str(n)
        n1=list(n3)
        value=0
        l=len(n1)
        for i in range(0,l):
            digit=n1.pop()
            nums=["0","1","2","3","4","5","6","6","7","8","9"]
            if digit in nums:
                value+=int(digit)*pow(16,i)
            elif digit=="A" or digit=="a":
                value+=10*pow(16,i)
            elif digit=="B" or digit=="b":
                value+=11*pow(16,i)
            elif digit=="C" or digit=="c":
                value+=12*pow(16,i)
            elif digit=="D" or digit=="d":
                value+=13*pow(16,i)
            elif digit=="E" or digit=="e":
                value+=14*pow(16,i)
            elif digit=="F" or digit=="f":
                value+=15*pow(16,i)
        dec+=value
        if T2==10:
            print(dec)
        elif T2==2:
            n2=bin(dec)
            print(n2)
        elif T2==8:
            n2=oct(dec)
            print(n2)
        else:
            print("Enter valid number.")
    else:
        print("1).Enter 2 for binary")
        print("2).Enter 8 for octal.")
        print("3).Enter 10 for decimal.")
        print("4).Enter 16 for hexadecimal.")
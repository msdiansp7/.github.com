n=int(input("Enter the number : "))
T1=int(input("From base : "))
T2=int(input("To base : "))
if T1==10:
    if T2==2:
        n1=bin(n)
        print(n1)
    elif T2==8:
        n1=oct(n)
        print(n1)
    elif T2==16:
        n1=hex(n)
        print(n1)
    else:
        print("Enter valid base number.")
elif T1==2:
    dec=0
    n1=list(n)
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
    n1=list(n)
    values=0
    l=len(n1)
    for i in range(0,l):
        digit=n1.pop()
        if int(digit)!=8 and int(digit)!=9:
            value+=num*pow(8,i)
            print(value)
        dec+=value
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
    n1=list(n)
    values=0
    l=len(n1)
    for i in range(0,l):
        digit=n1.pop()
        if int(digit)!=8 and int(digit)!=9:
            value+=num*pow(8,i)
        print(value)
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
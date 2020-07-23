##list comprehension
#squares=[i**2 for i in range(1,11)]
#print(squares)
#negative=[-i for i in range(-11,11)]
#print(negative)
#names=['shubham','amit','satish','nikhil']
#fchar=[names[i][0] for i in range(0,len(names))]
#print(fchar)
#n1,n2,n3=input("Enter your 3 friend name : ").split(",")
#names=[n1[-1::-1],n2[-1::-1],n3[-1::-1]]
#print(names)
#even=[i for i in range(1,11) if i%2==0]
#print(even)
#print([i for i in range(1,11) if i%2==0])
#odd=[i for i in range(1,11) if i%2!=0]
#print(odd)
#print([i for i in range(1,11) if i%2!=0])
#data=[True,False,'sh',56,6,3.0,7]
#numstr=[str(i) for i in data if type(i)==type(7) or type(i)==type(2.0)]
#print(numstr)
#new=[i*2 if (i%2==0) else -i for i in range(1,11)]
#print(new)
#nested_list=[list(range(1,4)) for i in range(1,4)]
#print(nested_list)
#sq={"square of " + str(i)+ " is " +str(i**2) for i in range(1,11)}
#print(sq)
#name=input("Enter your name : ")
#chars={name[i] : name.count(name[i]) for i in range(0,len(name))}
#print(chars)
#cubes={i : (i**2 if i%2==0 else i**3) for i in range(1,11)}
#print(cubes)
#def sum(*args):
#    total=0
#    for i in args:
#        total+=i
#    return total
#print(sum(1,4,5,7,9,6,4,5,1))
#def normal_args(n1,*args):
#    print(n1)
#    print(args)
#    multiply=1
#    for i in args:
#        multiply*=i
#    return multiply
#print(normal_args(0,1,2,3,4,5))
#nums=[1,3,4,2,6,7,10]
#def sum(*args):
#    total=0
#    for i in args:
#        total+=i
#    return total
#print(sum(*nums))
#n=[]
#n1,n2,n3,n4,n5=input("Enter any five numbers : ").split(",")
#n.append(int(n1))
#n.append(int(n2))
#n.append(int(n3))
#n.append(int(n4))
#n.append(int(n5))
#def cubes(*args):
#    cubes=[]
#    for i in args:
#        if args:
#            cubes.append(i**3)
#        else:
#            print("please enter some numbers !!")
#    return cubes       
#print(cubes(*n))
#print(cubes(*[1,2,3,4]))
#def kwarg(**kwarg):
#    return kwarg
#print(kwarg(name ="shubham",
#age=26,
#pass1="Msd@123",email="msdiansp@gmail.com"))
#d={'name' : 'shubham','age' : 24}
#print(kwarg(**d))
#def order(name,*args,age=20,**kwargs):
#    print(name)
#    print(args)
#    print(age)
#    print(kwargs)
#order('shubham',14,10,2000,pass1='Msd@123')
#names=["shubham","amit","satish","nikhil"]
#def string(*args):
#    capitalize=[]
#    for j in args:
#        j=j[-1::-1]
#        capitalize.append(j.title())
#        
#    return capitalize
#print(string(*names))
#def reverse(*args,**kwargs):
#    if kwargs.get("rev_string"):
#        return [i[-1::-1].title() for i in args]
#print(reverse(*names,rev_string =True))    
        
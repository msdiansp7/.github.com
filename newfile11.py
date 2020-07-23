#def add(a,b):
#    return a+b
#add2=lambda a,b : a*b
#print(add2(3,5))
#even=lambda a: a%2==0
#print(even(72))
#lastChar=lambda s: s[-1]
#print(lastChar('shubham'))
#func=lambda s: 'There you are !!' if len(s)>5 else False
#print(func('shubham'))
#names=['shubham','amit','satish']
#for name in enumerate(names):
#    print(f"{name}")
#for n,name in enumerate(names):
#    print(f"{n} ---> {name}")
#names=['shubham','amit','satish']
#def func(s,*args):
#    if s in args:
#        print(f"{s} -->{args.index(s)}")
#    else:
#        print("-1")
#func('shubham',*names)
#def fun(s,*args):
#    for n,name in enumerate(args):
#        if s in name:
#            print(f"{s} -- {n}")
#        else:
#            print("-1")
#fun("amit",*names)
#def fun(n,name):
#    for no,names in enumerate (n):
#        if name==names:
#            return f"{no} --> {names}"
#        return -1
#print(fun(names,"shubham"))
#n=[0,1,2,3,7,5]
#def square(a):
#    return a**2
#print(list(map(square,n)))
#print(list(map(lambda a:a**3,n)))
#sq=[i**2 for i in n ]
#print(sq)
#n=[7,3,9,2,0,7,5,4,2,8,0]
#def even(a):
#    return a%2==0
#evens=list(filter(even,n))
#evens=tuple(filter(even,n))
#print(evens)
#user=["shubham","amit","satish","nikhil"]
#password=["msd@123","amit@7","satish@3","nikhil@10"]
#d=dict(list(zip(user,password)))
#print(d)
#username=input("Enter your username :\n")
#password=input("Enter your password :\n")
#def login(N,P,**kwargs):
#    if N in kwargs and P in kwargs.values():
#        print(f"Welcome {N}!!!!")
#    else:
#        print("Enter valid username and password.")
#login(username,password,**d)
#n=[(11,2,3),(3,14,5),(35,6,7),(7,8,9)]
#n1,n2,n3=list(zip(*n))
#print(n1)
#print(n2)
#print(n3)
#for pair in zip(n1,n2):
#    print(max(pair))
#    print(min(pair))
#n=[[1,2,3],[3,6,1],[11,3,0],[4,100,679193]]
#avg=lambda a,b,c:(a+b+c)/3
#print(avg(n[0][0],n[1][0],n[2][0]))
#def avg(n1,n2,n3):
#    list(zip(n1,n2))
#    for pair in zip(n1,n2,n3):
#        print(sum(pair)/len(pair))
#avg(n[0],n[1],n[2])
#def avg(*args):
#    list(zip(*args))
#    for pair in zip(*args):
#        print(sum(pair)/len(pair))
#avg(*n)
#avg=lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]
#print(avg(*n))

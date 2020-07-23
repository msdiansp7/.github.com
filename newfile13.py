#def sq(a):
#    return a**2

#l=list(range(1,11))
#print(l)
#def my_fun(func,l):
#    squares=[]
#    for i in l:
#        squares.append(func(i))
#    return squares
#print(my_fun(lambda a:a,l))
#print(my_fun(sq,l))
#print(my_fun(lambda a:a**3,l))
#for i in range(1,11):
#    print(my_fun(lambda a:a**i,l))
#def outer_F():
#    def inner_F():
#        print("This is an inner function.")
#    return inner_F
#func=outer_F()
#func()
#def F1(msg):
#    def F2():
#        print(f"{msg}")
#    return F2
#F3=F1("Hi there !!!")
#F3()
#def power(x):
#    def base(a):
#        return a**x
#    return base
#ans=power(5)
#print(ans(2))
#def f1(any):
#    def f2():
##    def f2(*args,**kwargs):
#        print("Hi there ! ")
#        any()
##        return any()            
#    return f2
#@f1
#def f3():
#    print("I am using WhatsApp.")
##def f3(a,b):
##    return a+b
##    print("I am using WhatsApp.")
#f3()
#f=f1(f3)
#f()
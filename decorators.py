#from functools import wraps
#import time
#def f1(any):
#    @wraps(any)
#    def f2(*args,**kwargs):
#        print("You are shubham.")
#        return any()
#    return f2
#@f1
#def f3(a):
#    return a**2
#    print("I am shubham.")
#print(f3.__name__)
#def adding(any):
#    @wraps(any)
#    def wrapper(*args,**kwargs):
#        print(f"You are calling {any.__name__} function.")
#        return any(*args,**kwargs)
#    return wrapper
#@adding
#def add(a,b):
#    """This function takes two arguments and return their sum"""
#    print(add.__doc__)
#    print(a+b)
#    
#add(4,5)
#t1=time.time()
#def Time(fun):
#    @wraps(fun)
#    def other(*args):
#        print(f"this is a {fun.__name__} function.")
#        return fun()
#    return other
#@Time
#def func():
#    """This is something."""
#    print(func.__doc__)
#    print("I am doing well.")
#func()
#t2=time.time()
#print(f"This function takes {t2-t1} seconds to load.")
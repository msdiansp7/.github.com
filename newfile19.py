#while True:
#    try:
#        age=int(input("Enter your age : "))
#        name=input("Enter your name : ")
#    except ValueError:
#        print("Enter integer value.")
#    except:
#        print("Invalid input!!")
#    else:
#        print(f"Hello,{name}.")
#        break
#    finally:
#        print("loading.............")
#    
#if age < 18:
#    print("Sorry,you can\'t play this game!")
#else:
#    print("You can play this game.")
#while True:
#    try:
#        a=int(input("Enter first number : "))
#        b=int(input("Enter second number : "))
#    except ValueError as msg:
#        print("Please enter an integer.")
#        print(msg)
#    except:
#        print("Please enter valid input.")
#    else:
#        print ("Finishing up!!!")
#        break
#    
#def devide(a,b):
#    return a/b
#try:
#    print(devide(a,b))
#except ZeroDivisionError as msg:
#    print("Can\'t devide by Zero.")
#    print(msg)
#class NameTooShortError(ValueError):
#    pass
#def validate(name):
#    if len(name)< 8:
#        raise NameTooShortError("Name is too short.")
#    else:
#        print(name)
#username=input("Enter your name : ")
#validate(username)
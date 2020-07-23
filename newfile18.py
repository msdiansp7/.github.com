#def add(a,b):
#    if (type(a)==int) and (type(b)==int):
#        return a+b
#    else:
#        raise TypeError("Invalid input type.")
#print(add(3,"shubham"))
#def add(a,b):
#    if (type(a)==int) and (type(b)==int):
#        return a+b
#    else:
#        return "Invalid input type."
#print(add(3,"shubham"))
#class Animal:
#    def __init__(self,name):
#        self.name=name
#        
#    def sound(self):
#        raise NotImplementedError("You have define this method in subclasses.")
#        
#class Dog(Animal):
#    def __init__(self,name,breed):
#        super().__init__(name)
#        self.breed=breed
#        
#    def sound(self):
#        return "Bhao bhou"
#        
#class Cat(Animal):
#    def __init__(self,name,breed):
#        super().__init__(name)
#        self.breed=breed
#        
#    def sound(self):
#        return "Meo meo"
#        
#Bark=Dog("Moti","german sheford")
#print(Bark.sound())
#class Mobile:
#    def __init__(self,name):
#        self.name=name
#        
#        
#class Mobilestore:
#    def __init__(self):
#        self.mobiles=[]
#        
#    def add_mobiles(self,new_mobile):
#        if isinstance(new_mobile,Mobile):
#            self.mobiles.append(new_mobile)
#        else:
#            raise TypeError("new mobile should be method of Mobile class.")

#one=Mobile("onePlus 6")
#two=Mobile("Samsung Galaxy J2 Pro")
#samsung="Samsung Galaxy J2 Pro"
#New=Mobilestore()
#New.add_mobiles(two)

#mob=New.mobiles
#print(mob[0].name)
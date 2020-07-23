#class Users:
#    def __init__(self,fname,lname,age):
#        print("This is the my class.")
#        self.fname=fname
#        self.lname=lname
#        self.age=age
#P1=Users("shubham","patil",20)
#P2=Users("Amit","patil",22)
#print(P1)
#print(P1.fname)
#class Mobile:
#    def __init__(mobiles,name,OS,model,price):
#        print("Here is the product information.")
#        mobiles.name=name
#        mobiles.OS=OS
#        mobiles.model=model
#        mobiles.price=price
#        mobiles.info=name+" "+OS+" "+model+" "+price
#M1=Mobile("Samsumg","Android","Galaxy J2 Pro",7999)
#M2=Mobile("Nokia","Android","N10",10000)
#print(M1.name)
#print(M2.price)
#class User:
#    def __init__(self,fname,lname,age):
#        self.fname=fname
#        self.lname=lname
#        self.age=age
#    def fullname(self):
#        return f"{self.fname} {self.lname}."
#U=User("Shubham","Patil",20)
#print(U.fname)
#print(U.fullname())
#print(User.fullname(U))
#l=[1,2,3,4]
#list.clear(l)
#print(l)
#class Mobile:
#    def __init__(mobiles,name,OS,model,price):
#        print("Here is the product information.")
#        mobiles.name=name
#        mobiles.OS=OS
#        mobiles.model=model
#        mobiles.price=max(price,0)
#        if price > 0:
#            mobiles.price=price
#        else:
#            mobiles.price=0
#        mobiles.price=price
#        mobiles.info=name+" "+OS+" "+model+" "+str(price)
#    def discount(mobiles,n):
#        mobiles.discount=mobiles.price*((100-n)/100)
#        return mobiles.discount
#M1=Mobile("Samsumg","Android","Galaxy J2 Pro",7999)
#M2=Mobile("Nokia","Android","N10",10000)
#print(M1.price)
#class Circle:
#    pi=3.14
#    class_instance=0
#    def __init__(self,radius):
#        Circle.class_instance+=1
#        self.radius=radius
#    @classmethod
#    def count_inst(cls):
#        return f"You have created {cls.class_instance} Circle instances."            
#    def circumference (self):
#        return 2*self.radius*Circle.pi
#    def CArea(self):
#        return Circle.pi*(self.radius**2)
#    class_instance+=1
#C=Circle(24)
#C1=Circle(50)
#C2=Circle(10)
#Circle.pi=0
#print(C1.circumference())
#print(C2.CArea())
#print(C1.__dict__)
#print(Circle.class_instance)
#print(Circle.count_inst())
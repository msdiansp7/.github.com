#class Mobile:
#    def __init__(self,name,price,model):
#        self.name=name
#        self._price=price
#        self.model=model
#    @property
#    def fullname(self):
#        return f"{self.name} {self.model} at Rs.{self.price}/- only"
#    @property
#    def price(self):
#        return self._price
#    @price.setter
#    def price(self,new_price):
#        self._price=max(new_price,0)
#    @staticmethod
#    @classmethod
#    def fullname2():
#        print(f"{self.name} {self.model}")
#    
#M1=Mobile("samsung",7000,"Galaxy J2 pro")
#M1.price=7009
#price=-7009
#print(M1.price)
#print(M1.fullname())
#print(M1.fullname2)
#class Smartphone(Mobile):
#    def __init__(self,name,price,model,ram,external_memory,rear_camera):
#        Mobile.__init__(self,name,price,model)
#        super().__init__(name,price,model)
#        self.ram=ram
#        self.external_memory=external_memory
#        self.rear_camera=rear_camera

#S1=Smartphone("Nokia",10000,"1100","4GB","32GB","56MP")
#print(S1.fullname)
#print(isinstance(S1,list))
#print(isinstance(S1,Smartphone))
#print(issubclass(Mobile,Smartphone))
#print(issubclass(Smartphone,Mobile))
#class A:
#    
#    def CA(self):
#        return "Shubham"
#        
#    def CA2(self):
#        return "Amit"
#        
#class B:
#    
#    def CB(self):
#        return "Shubham1"
#        
#    def CB2(self):
#        return "Amit2"
#        
#class C(A,B):
#    
#    def CC(self):
#        return "hello"
#A1=A()
#print(A1.CA2())
#print(C.__mro__)
#class A:
#    def A(self):
#        return "shubham"
#        
#    def __str__(self):
#        return "Msdian"
#        
#    def __repr__(self):
#        return "Msdianshubham7"
#A1=A()
#print(A1)
#print(str(A1))
#print(repr(A1))
#class S:
#    
#    def __add__(self,other):
#        return self.price + other.price
#        
#    def __mul__(self,other):
#        return self.price * other.price
#        
#S1=S()
#print(S1 * S1)
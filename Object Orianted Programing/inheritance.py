class Phone:
     def __init__(self,brand,name,price):#base class/parent class
        self.brand=brand
        self.name=name
        self.price=price=max(price,0)
    

     def make_a_call(self,number):
        return f"calling..........{number}"

     def full_name(self):
        return f"full name is {self.brand}..{self.name}"

class Smartphons(Phone):#derived class / chield class
     def __init__(self,brand,name,price,ram,rom,camera):
        # two ways
        # Phone.__init__(self,brand,name,price)   #uncommonway
        super().__init__(brand,name,price)
        self.ram=ram
        self.rom=rom
        self.camera=camera

    

    
Phone1=Phone("Apple","ios7",36000)
Phone2=Smartphons("Samsung","s27",30000,4,6,98)

print(Phone1.full_name())
print(Phone2.full_name())
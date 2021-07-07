# Method REsolution Order
# use help functiom to see method resolution order
class Phone:
     def __init__(self,brand,name,price):#base class/parent class
        self.brand=brand
        self.name=name
        self.price=price=max(price,0)
    

     def make_a_call(self,number):
        return f"calling..........{number}"

     def full_name(self):
        return f"full name is {self.brand}..{self.name}"

class Smartphone(Phone):
      def __init__(self,brand,name,price,ram,rom,camera):
          super().__init__(brand, name, price)
          self.ram=ram
          self.rom=rom
          self.camera=camera
class Flegishipphon(Smartphone):
      def __init__(self,brand,name,price,ram,rom,camera,fcamera):
          super().__init__(brand,name,price,ram,rom,camera)
          self.fcamera=fcamera       
    #   method overriting 
      def full_name(self):
            return f"This Is Flagsheep Phone {self.brand}...{self.name}....{self.rom}....{self.fcamera}" 

smart1=Smartphone("samsung","ASDD",23456,32,43,65)
smart2=Flegishipphon("apple","ios",23453336,33332,33343,33365,33453334)
# print(smart1.full_name())       
# print(smart2.full_name())     
# print(help(Flegishipphon))  
smart0=Phone("eee","eeree",98766)
# isinstance function is use to find given object is that class or not
# print(isinstance(smart2,Flegishipphon))
# print(isinstance(smart2,Smartphone))
# print(isinstance(smart2,Phone))
# print(isinstance(smart1,Flegishipphon))
# print(isinstance(smart1,Smartphone))
# print(isinstance(smart0,Flegishipphon))
# print(isinstance(smart0,Smartphone))
# print(isinstance(smart0,Phone))

# issubclass function is use to find the given class is subclass of onother class or not
print(issubclass(Smartphone,Phone))
print(issubclass(Phone,Smartphone))
print(issubclass(Smartphone,Flegishipphon))
print(issubclass(Flegishipphon,Smartphone))
print(issubclass(Phone,Flegishipphon))
print(issubclass(Flegishipphon,Phone))
class Phone:
     def __init__(self,brand,name,price):#base class/parent class
        self.brand=brand
        self.name=name
        self.price=price=max(price,0)
    

     def make_a_call(self,number):
        return f"calling..........{number}"

     def full_name(self):
        return f"full name is {self.brand}..{self.name}"

    #  dunder methods   
    # str,repr 
   #   def __str__(self):
   #      return f"{self.brand} {self.price}"
   #   def __repr__(self):
   #      return f"{self.brand} {self.name} {self.price}"


my_phone=Phone("Apple","ios7",39000)
print(my_phone)
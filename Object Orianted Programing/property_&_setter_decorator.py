class Phone:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price=max(price,0)
        # self.complete_specification=f"brand name is {self.brand} model is {self.brand} {self.name} only in {self.price}"
    @property
    def complete_specification(self):
        return f"brand name is {self.brand} model is {self.brand} {self.name} only in {self.price}"
    @property
    def price(self):
        return self.price
    @price.setter
    def price(self,new_price):
        self.price=max(new_price,0)

    def make_a_call(self,number):
        return f"calling..........{number}"

    def full_name(self):
        return f"full name is {self.brand}..{self.name}"

Phone1=Phone("Apple","ios7",-36000)
print(Phone1.brand)
print(Phone1.name)
print(Phone1.price)
Phone1.price=-1000000000000
print(Phone1.price)
print(Phone1.complete_specification)
print(Phone1.make_a_call(8080358145))
print(Phone1.full_name())


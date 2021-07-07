class Phone:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price

    def make_a_call(self,number):
        print(f"calling..........{number}")

    def full_name(self):
        return f"full name is {self.brand}..{self.name}"

    def sent_message(self):
        pass
    # _name is the convention for private name
    # __name__ its is dunders methods or magic methods
    # name mangaling, __name (not a convention)
# create object

Apple=Phone("Apple","ios7","35k")
Samsung=Phone("Sansung","dudes7","15k")
print(Apple.make_a_call("8983805184"))
print(Apple.full_name())
print(Apple.price)
Apple.price= -10000
print(Apple.price)
print(Samsung.full_name())

 
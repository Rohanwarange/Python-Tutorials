class Laptops:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
        self.name=brand_name +" " + model_name

l1=Laptops("HP","pavilion",890000)
l2=Laptops("Dell","abcd987",540000)
print(l2.model_name)
print(l1.price)
print(l1.name)


# class
class Person:
    # init method or constructor
    def __init__(self,first_name,last_name,age):
        print("constructor called")
        # instance variable
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
p1=Person("Rohan","warange",24)
p2=Person("rohan.123","rwCreation",20)        

print(p1.first_name)
print(p2.first_name)
print(p2.last_name)
print(p1.age)
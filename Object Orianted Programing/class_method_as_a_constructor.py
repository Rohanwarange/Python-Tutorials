class Person:
    counter=0
    def __init__(self,first_name,last_name,age):
        Person.counter+=1
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

        
# create object from class method
    @classmethod
    def from_string(cls,string):
        first,last,age=string.split(",") 
        return cls(first,last,age) 

    @classmethod
    def count_instances(cls):
        return f"You have created by classs method {cls.counter}"
    def full_name(self):
        return f"{ self.first_name} {self.last_name}"
    def is_above_18(self):
        return self.age>=18   
p1=Person("Rohan","Warange",24)
p2=Person("Rohan.123","warange.123",20)
print(p2.full_name())       
print(p2.is_above_18())    
print(f"you have created .....{Person.counter} instance of person class")  
print(Person.count_instances())
p4=Person.from_string("pavi,manyar,24")
print(p4.full_name())
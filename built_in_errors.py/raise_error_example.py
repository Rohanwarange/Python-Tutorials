class Animal:
     def __init__(self,name):
        self.name=name

     def sound(self):
         raise NotImplementedError("you have to define sound method in each class")

class Dog(Animal):
    def __init__(self, name,bread):
        super().__init__(name)
        self.bread=bread
    def sound(self):
        return "bho bho"


class Cat(Animal):
    def __init__(self, name,bread):
        super().__init__(name)        
        self.bread=bread
    def sound(self):
        return "mao mao"

dogy=Dog("bony","pug")
manya=Cat("Many","leg")      
print(dogy.sound())
print(manya.sound())
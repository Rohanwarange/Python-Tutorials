class Circle:
    pi=3.14 #instance variable
    def __init__(self,radius):
        self.radius=radius
    def Circumference(self):
        return 2*self.radius*Circle.pi
    def Area(self):
        return (self.radius*Circle.pi)**2
c1=Circle(24)           
c2=Circle(4)
print(c1.Circumference())
print(c2.Circumference())
print(c1.Area())
print(c2.Area())
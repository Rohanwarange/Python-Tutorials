#  multyple inheritance

class A:
      def class_a_method(self):
          return "class a meyhod"
      def hello(self):
          return "hello from class a"
class B:
      def class_b_method(self):
        return "class b method"  
      def hello(self):
          return "hello from class b" 
class C(A,B):
      pass              

a=A()
b=B()
c=C()
print(a.class_a_method())
print(b.class_b_method())
print(c.class_a_method())
print(c.class_b_method())
print(a.hello())
print(c.hello())
print(b.hello())
def add(a,b):
    if type(a) and type(b)==int:
       return a+b
    raise TypeError("error")
print(add(5,3))    
print(add("5","3"))    
def square(a):
    return a**2
s=square
print(s(7))    
print(s.__name__)
print(square.__name__)
print(s.__doc__)
print(dir())
# print(s.__help__)

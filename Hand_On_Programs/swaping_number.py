# swaping number using another variable

# a=int(input("Enter The NUmber a : "))
# b=int(input("Enter The NUmber b : "))
# temp=a
# a=b
# b=temp
# print(f"after seaping {a}")
# print(f"after swaping {b}")


# by using same variable 

a=int(input("Enter The NUmber a : "))
b=int(input("Enter The NUmber b : "))
a=a+b
b=a-b
a=a-b
print(f"after seaping {a}")
print(f"after swaping {b}")

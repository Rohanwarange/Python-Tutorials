# factorial by using math module 
# import math
# n=int(input("Enter the Number : "))
# print(math.factorial(n))

# factorial by using recursion function 
n=int(input("Enter The NUmber : "))
def fact(n):
    if n==0:
       return 1
    else:
        factorial=n*fact(n-1)
    return factorial
print(f" factorial of {n} is {fact(n)}")      

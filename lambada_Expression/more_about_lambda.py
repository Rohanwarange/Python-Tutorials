# def odd_even(num):
#     if num%2==0:
#         return True
#     return False
# print(odd_even(5))        

# is_even=lambda a :a%2==0
# print(is_even(8))

# last_char=lambda a:a[-1::]
# print(last_char("Rohan"))

# lambda with if else
# def fun(s):
#     if len(s)>=5:
#         return True
#     return False
# print(fun("Rohan"))        

func1=lambda s:True if len(s)>5 else False
print(func1("Rohan"))
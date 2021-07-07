# def is_even(a):
#     return a%2==0
numbers=[3,4,2,1,5,6,9,8,10] 
# print(list(filter(is_even,numbers)))

# with lambada function
print(list(filter(lambda a:a%2==0,numbers)))

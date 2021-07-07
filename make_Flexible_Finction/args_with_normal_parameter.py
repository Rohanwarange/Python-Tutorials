# def multiply(*args):
#     multiplynum=1
#     for i in args:
#         multiplynum*=i
#     return multiplynum
# print(multiply(1,2,3,4))  

# normal parameter with args

def multiply(num,num1, *args):
    multiplynum=1
    for i in args:
        multiplynum*=i
    return multiplynum
print(multiply(2,2,3,4))        

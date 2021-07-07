def multiply(*args):
    multiplynum=1
    for i in args:
        multiplynum*=i
    return multiplynum
num=[2,2,3,4]    

print(multiply(*num))
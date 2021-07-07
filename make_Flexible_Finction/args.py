def total(a,b):
    return a+b
print(total(5,5))  

# *args

def total(*args):
    print(args)
    total=0
    for num in args:
        total+=num
    return total
print(total(1,2,3,4,5))
# create a generator with generator function
# def num(a):
#     for i in range(1,a+1):
#         print(i)
# num(10)  

# generators

def num(a):
    for i in range(1,a+1):
        yield(i)
num(10)     
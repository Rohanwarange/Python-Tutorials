from functools import wraps
def decorator_function(any_func):
    @wraps(any_func)
    def wrappeer(*args,**kwargs):
        data_type=[]
        for args in args:
            data_type.append(type(args)==int)
        if all(data_type):
           return any_func(*args,**kwargs)
        else:
            print("invalid")    
        return any_func()
    return wrappeer




@decorator_function

def add_all(*args):
    total=0
    for i in args:
        total+=i
    return total  

print(add_all(2,3,4,5,6,7,8))     
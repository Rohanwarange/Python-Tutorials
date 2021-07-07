def decorator_func(any_function):
    def wrapper_function(*args,**kwargs):
        print("this is awasom function")
        return any_function(*args,**kwargs)
    return wrapper_function

    # this is awasom function 
@decorator_func
def func(a):
    print(f"This is function with argument{a}")    
# def func():
#     print(f"This is Function")    
@decorator_func
def add(a,b):
    return a+b
print(add(2,3))    
from functools import wraps

def decorator_fuction(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print("Thsi is Awasom Function ")
        return any_function()
    return wrapper_function

@decorator_fuction
def func1():
    print("This is india")

def func2(): 
    print("This is Austrelisa")

func1()
func2()               
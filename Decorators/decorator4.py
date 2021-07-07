from functools import wraps
def decorator_fun(any_function):
    @wraps(any_function)
    def wrapper_function(*args,**kwargs):
        print(f"You are calling {any_function.__name__}")
        print(f"{any_function.__doc__}")
        return any_function(*args,**kwargs)
    return wrapper_function
@decorator_fun 


def add(a,b):
    """ this function will tack two function as an argument and writen their adition"""
    return a+b
print(add(4,5))
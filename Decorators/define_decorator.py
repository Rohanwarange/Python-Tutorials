# decorator- enhance functionality of other function 

# this is awasom function 
def decorator(any_function):
    def wrapper_function():
        print("This is awasom function : ")
        return any_function()
    return wrapper_function    

@decorator
def func1():
    print("this is function 1")
func1()    


def func2():    
    print("this is function 2")

# var=decorator(func1)
# var()   
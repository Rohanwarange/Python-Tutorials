# use@ for decorators
def decorator_function(any_function):

    def wrapper_function():
        print("this is awasom i love it!!!")
        any_function()
    return wrapper_function 
@decorator_function    #shortcut   
def func1():
    print("i love my villege")

def func2():
    print("i love my india")
func1()
func2()
# var=decorator_function(func1)
# var()
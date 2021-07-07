# calculate time 
from functools import wraps 
import time
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper(*args,**kwargs):
        t1=time.time() 
        a= any_function(*args,**kwargs)
        t2=time.time() 
        T=t2-t1 
        print(f"This Function tackes {T} ninuts to complete")
        return a
 
    return wrapper 

@decorator_function
def fuct():
    print("this is funct")
fuct()    
 


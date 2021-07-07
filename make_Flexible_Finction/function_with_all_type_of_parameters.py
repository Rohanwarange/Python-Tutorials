# Function With All parameter
# very important to understand

# PADK

def func(name,*args,last_name="unknown",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func("Roahn",1,2,3,4,"Raj",a=1,b=2)
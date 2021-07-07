# **kwargs as a parameter
def func(**kwargs):
    # print(kwargs)
    for k,v in kwargs.items():
        print(f"{k}:{v}")
func(first_name ="harshist",last_name="bvasista") 


# keyword argument

def func(name,**kwargs):
    # print(kwargs)
    for k,v in kwargs.items():
        print(f"{k}:{v}")
func("Rohan",first_name ="harshist",last_name="bvasista") 


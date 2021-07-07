# def validate(name):
#     if len(name)<8:
#         raise ValueError("name is true short")
# username=input("Enter Your name")     
# validate(username)   
# def validate(name):
#     if len(name)<8:
#         raise ValueError("name is true short")
# username=input("Enter Your name")     
# validate(username) 



class NameTOOShore(ValueError):
    pass
def validate(name):
    if len(name)<8:
        raise NameError("name is true short")
username=input("Enter Your name")     
validate(username)   



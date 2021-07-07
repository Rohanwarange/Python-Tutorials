# by using reverse 
# str=input("Enter the String : ")
# def reverse_str(str):
#     return (reversed(str))

# print(reverse_str(str))    

# by using slising
# 
# using function 
def reverse_string(str):
    reverse_str=""
    for i in str:
        reverse_str=i+reverse_str
    return reverse_str
print (reverse_string("Rohan"))    
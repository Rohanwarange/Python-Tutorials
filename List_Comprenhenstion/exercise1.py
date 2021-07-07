# define a function thant take list of strings
# list containing reverse of every string

# using list comptrhenstion
# using normal list

# string=["Rohan","Sanjay","Warange"]
# reverses1=[]
# for i in string:
#     reverses1.append(i[::-1])
# print(reverses1)    


string=["Rohan","Sanjay","Warange"]
reverse_string=[i[::-1] for i in string]
print(reverse_string)
# steps for debuging
# 1) set trace 
# 2) execute code line by line

import pdb

pdb.set_trace()
name=input("Enter Name")
age1=int(input("Enter age"))
print(f"name is {name} age is {age1}")
age2=age1+5
print(f"name is {name} age is {age2}")

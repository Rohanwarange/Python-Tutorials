# we can use enumerate function with loop to track possion
# items in iterable

# without enumerate function
# names=["abc","pqr","xyz"]
# pos=0
# for i in names:
#     print(f"{pos}:{i}")    
#     pos+=1


# enumerate function

# names=["abc","pqr","xyz"]

# for pos,name in enumerate(names):
#     print(f"{pos} :{name}")

l=["abc","pqr","xyz"]
def find_position(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
    return -1    
print(find_position(l,"abc"))
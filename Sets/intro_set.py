# Set Data type
# unorder collection of uniqe items
s={1,2,3,4,4}
print(s)

# set uses...............................
# remove duplicate
l=[1,2,3,4,4,3,2,1,1,2,3,4,4,3,2,1,345,22,678,33,5,42,8,5,2,4,5,6,4,3,5,7,4,3,4,5,6,4]
s2=set(l)
# print(s2)

# add element in set
s.add(9)
print(s)

# remove from set
s.remove(4)
print(s)

s.discard(4)

# clere method
s.clear()
print(s)

# copy method()
s5=s.copy()
print(s5)

# store in set
# int,strig,float
# list,array,tuple,dictionary are not stored in set


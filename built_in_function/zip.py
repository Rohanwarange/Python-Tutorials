# zip Function
# user_id=["user1","user2","user3"]
# names=["rohan","sanjay","warange"]

# print(list(zip(user_id,names)))

# exaample=[("a ",1),("b",2)]
# print(dict(exaample))

# *operater with zip
L=[(8,4),(8,9),(5,6),(3,4),(1,2)]
l1,l2=(list(zip(*L)))
print(l1)
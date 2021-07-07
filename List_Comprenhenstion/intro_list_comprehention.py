# list_comprehention
# Create a list of spqares frome 1 to 10
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)

squares2=[ i**2 for i in range(1,11)]
print(squares2)

negative_num=[-i for i in range(1,11)]
print(negative_num)
 
names=["Rohan","Sanjay","Warange"]
new_names=[i[0] for i in names]
print(new_names)
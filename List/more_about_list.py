# generate list with range function

numbers=list(range(0,11))
print(numbers)

# pop method

print(numbers.pop())

# index method

print(numbers.index(9))

# past list to the function

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
numbers=list(range(0,11))    
print(negative_list(numbers))        
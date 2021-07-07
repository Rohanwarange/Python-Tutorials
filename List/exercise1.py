def square_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
numbers=list(range(0,11))
print(square_list(numbers))    

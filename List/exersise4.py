numbers=[1,2,3,4,5,6,7,8,9,10]
def even_odd(l):
    even=[]
    odd=[]
    for i in range(len(l)):
        if l[i]%2==0:
            even.append(i)
        else:
            odd.append(i) 
    output=[even,odd]  
    return output          
             
print(even_odd(numbers))             
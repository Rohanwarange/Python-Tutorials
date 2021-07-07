def sublist(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
mixed=[[6,2,4,8],[3,5,7,4,6,4],2,4,6,7,7]   
print(sublist(mixed))         
# number=[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,32,43,54,65,78,89,444,567]
# print(list(map(lambda a:a*a,number)))


n=int(input("Enter the Number"))

l=[]
for i in range(n):
    a=list(map(int,input().strip().split()))
    print(a)
    l.append(a)
print(l)    

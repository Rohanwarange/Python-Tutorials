a=[]
n=0
for i in range(2):
    a.append(int(input()))
for i in range(1,min(a)+1):
    if a[0]%i==0 and a[1]%i==0:
        n+=1
print(n)  
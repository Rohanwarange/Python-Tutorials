n=int(input("Enter The Number : "))
a=1
b=3
c=a+b
if n==0 or n==1:
   print(a)
elif n==2:
     print(a,b)   
elif n==3:
     print(a,b,c)   
else:
    print(a,b,c,end=" ")
    for i in range(4,n+1):
        d=a+b+c
        a=b
        b=c
        c=d
        print(d,end=" ")
    print()
# cheack given number is amstrong or not 

# n=int(input("Enter The NUmber : "))
# result=0
# length=len(str(n))
# temp=n
# while temp>0:
#     r=temp%10
#     result+=r**length
#     temp//=10
# if n==result:
#    print("number is amstrong")
# else:     
#    print("number is not amstrong ")    
   

# fing amstrong number frong goven series 

n=int(input("Enter the number"))
for i in range(0,n+1):
    result=0
    temp=i
    while temp>0:
        length=len(str(i))
        r=temp%10
        result+=r**length
        temp//=10
    if i==result:
       print(i,end=",") 
print()       
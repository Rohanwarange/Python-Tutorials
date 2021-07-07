# enter the given number is prime or not 
n=int(input("enter the number : "))
for i in range(2,n+1):
    if n%i==0:
       print(f"{n} is not prime number ")
       break
else:
    print("number is prime ")    

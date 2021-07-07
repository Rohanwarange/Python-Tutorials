# fibonacci series by if else statement

# n=int(input("Enter the number : "))
# a=0
# b=1
# if n==1:
#    print(a,end=" ")
# else:
#    print(a,b,end=" ")
#    for i in range(2,n+1):
#       c=a+b
#       a=b
#       b=c
#       print(c,end=" ")   
#    print()  
# 
# fibonacii series by function
n=int(input("enter the number : "))
def fibonacci(n):
   a=0
   b=1
   if n==1:
      print(a)
   else:
      print(a,b,end=" ")
      for i in range(n-2):
         c=a+b
         a=b
         b=c
         print(c,end=" ")
      print()
print(fibonacci(n))      
          


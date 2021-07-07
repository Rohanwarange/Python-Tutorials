# str=input("Enter THe str : ")
# def palindrone(str):
#     reverse_str=str[::-1]
#     if reverse_str==str:
#         return ("String is palindrone")
#     else:    
#         return ("String is not palindrone")
# print(palindrone(str))        

lower=int(input("enter the lower number : "))
upper=int(input("enter the upper number : "))
for num in range(lower,upper+1):
    result=0
    for i in range(1,num):
        if (num%i)==0:
           result+=i
    result/=2       
    if num==result:
       print(num)  
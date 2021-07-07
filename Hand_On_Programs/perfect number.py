# perfect number by using for loop and if else 

# n=int(input("Enter The NUmber : "))
# result=0
# for i in range(1,n+1):
#     if n%i==0:
#        result+=i
# result=result/2       
# if result==n:
#    print("The number is perfect ")
# else:
#    print("The Number Is NOt perfect")   

# series of perfect number 
# Write Python 3 code in this online editor and run it.

#Correct

lower = int (input("Enter lower no."))
upper = int (input("Enter upper no."))

def perfect_no(lower,upper):
    result = 0
    for i in range(lower,(upper+1)):
        for j in range(1,i):
            if i%j == 0:
                result+=j
        
        
        if i == result:
            print(i)
            
        result=0
            
x = perfect_no(lower,upper)

print(x)


#wrong

# lower = int (input("Enter lower no."))
# upper = int (input("Enter upper no."))

# def perfect_no(lower,upper):
#     result = 0
#     for i in range(lower,(upper+1)):
#         for j in range(1,i):
#             if i%j == 0:
#                 result+=j
        
#         if i == result:
#             print(i)
            
# x = perfect_no(lower,upper)
# print(x)




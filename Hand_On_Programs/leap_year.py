n=int(input("enter leaf yeae: "))
if n%4==0:
    if n%100==0:     
       if n%400==0:
            print(f"{n} is leap year")             
    else:
         print(f"{n} not leap year")            
else:
     print(f"{n} not leap year")     







# 2nd code      
    
# num = int(input("Enter the year you want to check if is leap year or not: "))

# #take input year from the user to check if it is a leap year

# if(num%4 == 0):

#  #check if the number is divisible by 4 and if true move to next loop

#    if(num%100 == 0):

#      #check if the input year is divisible by 100 and if true move to next loop

#        if(num%400 == 0):

#            print("The year {} is a leap year".format(num))

#            #the input year is divisible by 4, 100 and 400, hence leap year.

#        else:

#            print("The year {} is Not a leap year".format(num))

#    else:

#        print("The year {} is a leap year".format(num))

#        #if the number is divisible by both 4 and 100 it is a leap year

# else:

#    print("The year {} is Not a leap year".format(num))

#    #if the input num is not divisible by 4 then it can not be a leap year altogether.

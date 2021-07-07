# make number guessing game
import random
n=random.randint(0,100)
print("Welcome TO number Guessing GAME")
name=input("Please Enter Your name : ")
print(f"hello {name}")
num=int(input("Enter The Number That You Want To Guess : "))
if num==n:
    print("You Guess Correct NUmber")
    print("You Won !!!")

else:
    print("You guess Wrong")    
    print("You Lost !!!")
print(f"Correct Number is : {n}")    
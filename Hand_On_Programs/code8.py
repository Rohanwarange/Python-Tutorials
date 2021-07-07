# Problem Statement

# FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:

# Coffee

# Espresso Coffee
# Cappuccino Coffee
# Latte Coffee
# Tea

# Plain Tea
# Assam Tea
# Ginger Tea
# Cardamom Tea
# Masala Tea
# Lemon Tea
# Green Tea
# Organic Darjeeling Tea
# Soups 

# Hot and Sour Soup
# Veg Corn Soup
# Tomato Soup
# Spicy Tomato Soup
# Beverages

# Hot Chocolate Drink
# Badam Drink
# Badam-Pista Drink
# Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):

# Welcome to CCD 

# Enjoy your

# Example 1:

# Input:
# c
# 1
# Output
# Welcome to CCD!
# Enjoy your Espresso Coffee!
# Example 2:

# Input
# t
# 9
# Output
# INVALID OUTPUT!

main_menu=[["Espresso Coffee","Cappuccino Coffee","Latte Coffee"],["Plain Tea","Assam Tea","Ginger Tea","Cardamom Tea","Masala Tea","Lemon Tea","Green Tea","Organic Darjeeling Tea"]
,["Hot and Sour Soup","Veg Corn Soup","Tomato Soup","Spicy Tomato Soup"],["Hot Chocolate Drink","Badam Drink","Badam-Pista Drink"]]
m=input()
n=int(input())
if m=="C" or m=="B" or m=="S" or "T":
    print("Welcome to CCD!")
    if m=="c" or m=="C":
        if n in range(0,4):
           print(f"enjoy your {main_menu[0][n-1]}!")
              
        else:
            print("INVALID OUTPUT!")   
              
    elif m=="s" or m=="S":
        if n in range(0,5):
          print(f"enjoy your {main_menu[2][n-1]}!")
        else:
            print("INVALID OUTPUT!")   
    elif m=="b" or m=="B":
        if n in range(0,4):
            print(f"enjoy your {main_menu[3][n-1]}!")
        else:
            print("INVALID OUTPUT!")   
    elif m=="t" or m=="T":
        if n in range(0,9):
            print(f"enjoy your {main_menu[1][n-1]}!")
        else:
            print("INVALID OUTPUT!")   
              

else:
    print("INVALID OUTPUT!")    



    

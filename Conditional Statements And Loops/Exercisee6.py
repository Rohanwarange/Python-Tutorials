win =43
guess=1
num=int(input("Enter the Number : "))
game_win =False
while game_win is not True:
     if num==win:
        print(f"Wow You Won in {guess} attempt")
        game_win=True
     else:
          if num<win:
              print("Too loo")
                  
          else:
              
               print("Too high")   
                           
          guess+=1                 
          num=int(input("Enter The Number Again : "))   

    

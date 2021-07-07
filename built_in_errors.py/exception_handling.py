while True:
     try:
         number=int(input("Enter The Number : "))

     except ValueError:
         print("Please Inter integer")

     except:
         print("Incorrect Input")
     else:
        print("This is Else Block")
        break
     finally:
        print("Thise is Finally")
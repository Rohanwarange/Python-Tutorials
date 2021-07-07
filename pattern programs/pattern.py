for row in range(6):
    for col in range(8):
        if ((col==0 or col==7) and row>1) or ((col>0 or col<7) and row==5) or ((col==1 or col==6) and row==1) or ((col==3 or col==4) and row==0) :
            print("*",end="")
        else:
            print(end=" ")
    print()         

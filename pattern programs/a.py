for i in range(8):
    for j in range(7):
        if ((i!=0 or i!=7) and (j==0 or j==6)) or ((j!=0 or j!=6) and i==0) or ((j>0 or j<6) and i==4):
            print("*",end="")
            
        else:
            print(end=" ")
    print()        
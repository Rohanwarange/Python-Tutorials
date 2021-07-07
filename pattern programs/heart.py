for i in range(7):
    for j in range(7):
        if (i==0 and (j>1 and j<5)) or ((j==0 or j==6) and i>1 and i<4) :
            print("*",end="")
        else:
            print(end=" ")
    print()        
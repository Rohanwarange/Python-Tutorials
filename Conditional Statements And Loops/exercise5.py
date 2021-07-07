name=input("Enter Your Name : ")
i=0
while  i<len(name):
    i=i+1
    print(f"{name[i]} : {name.count(name[i])}")
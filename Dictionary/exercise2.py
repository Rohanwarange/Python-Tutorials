user={}
names=input("Enter Your Name :  ")
ages=int(input("Enter Your Name :  "))
movies=input("Enter Your fev movies name :  ").split(",")
songs=input("Enter Your fev somgss name :  ").split(",")

user["names"]=names
user["ages"]=ages
user["movies"]=movies
user["songs"]=songs
print(user)

for key,value in user.items():
    print(f"{key}:{value}")



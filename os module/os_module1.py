import os
# os.getcwd #give current working directary
# print(os.mkdir("movies")) #create folder
# print(os.path.exists("movies")) #cheack folder exits or not
# if os.path.exists("movies3"):
#     print("Already exits")
# else:
#     os.mkdir("movies3")    

# open("file10.txt","a").close()
# to print list of directry

# print(os.listdir())
for i in os.listdir():
    print(os.path.join(os.getcwd(),i))
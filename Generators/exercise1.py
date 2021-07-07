# define generator function
# tacke a one number as an argument
# generate a sequence of even numbers frome one to that number

def even(a):
    for i in (1,a+1):
        if i%2==0:
            yield(i)
num=even(20)            

for i in num:
    print(i)           

for i in even(20):
    print(i)           

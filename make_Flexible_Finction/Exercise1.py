# define function
# input
# num,iterable(tupal,list)
# example
# num=[1,2,3]
# to_power 3

# output
# list=[1,8,27]

# if youser not pass any args then print ,message you have didnt pass any args

def cube(num,*args):
    if args:
        return[i**num for i in args]
    else:
        return "Yoy dont write anything"
nums=[1,2,3,4,5]             
print(cube(2,*nums))             
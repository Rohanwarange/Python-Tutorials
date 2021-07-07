# define func
# list
# return average
average=[]
def average_finder(l1,l2,l3):
    for pair in zip(l1,l2):
        average.append(sum(pair)/len(pair))
    return average
print(average_finder([1,2,3],[2,3,4],[6,7,4]))        
int=input("")
print(int)
l1=[1,2,3,4,5]
l2=[2,3,14,5,3,6,7,4]
def common(l1,l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common(l1,l2))            

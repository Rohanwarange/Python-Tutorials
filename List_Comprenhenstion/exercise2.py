# num to string
# define a function


def num_to_string(l):
    return[str(i) for i in l if (type(i)==int or type(i)==float)]
print(num_to_string([1,2,3,[234,432,5,3],2,6,4,7,4,3.1,1.3]))    
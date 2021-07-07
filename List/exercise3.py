numbers=['one','two','three','four','five','si',"seven","eight"]
def reverse_list(l):
    reverse=[]
    for i in l:
         reverse.append(i[::-1])
    return reverse
print(reverse_list(numbers))
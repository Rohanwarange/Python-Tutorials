string=input("Enter the word : ")
def pallindrone(string):
    if string==string[::-1]:
        return True
    return False    
print( pallindrone(string))
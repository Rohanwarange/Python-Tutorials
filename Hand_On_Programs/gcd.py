a=int(input("Enter The First number : "))
b=int(input("Enter The Second number : "))
def gcd_calcul(a,b):
    if b==0:
       return a
    else:
        return gcd_calcul(b,a%b)
print(gcd_calcul(a,b))        
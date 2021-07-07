def power(n,p):
    if (p==0):
       return 
    else:
       return n*(power(n,n-p))
print(power(2,2))       


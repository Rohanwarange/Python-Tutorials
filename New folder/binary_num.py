#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

import pdb
pdb.set_trace()

n = int(input())
binary=[]
while True:
    q=n//2
    rem=n%2
    binary.append(str(rem))
    n=q
    if n==0:
        break
binary= binary[::-1]
print(any)
# count=0
# a=[]    
# for i in range(len(binary)-1):
#         if binary[i]=="1":
#             count+=1
#             a.append(count) 
#         else:
#             count=0    
#             pass
               
# print(max(a))
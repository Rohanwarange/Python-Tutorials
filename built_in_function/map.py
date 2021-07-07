# number=[1,2,3,4,5,6,7]
# def square(a):
    #  return a**2

#  map(function name,iterable)   
# print(list(map(square,number)))

# with lambada
# print(list(map(lambda a:a**2,number)))

# list compenhesion
# square_new=[a**2 for a in number]
# print(square_new)

# without or listcompenhension

# for i in number:
#     print(list(i**2))
# l1=[]
# for i in range(3):
    #  l1.append(list(filter(int,input().strip())))
     
# a=0    
# for i in range(3):
#     for j in range(len(l1)):
#          a+=i
# print(a)    
# print(l1) 
# 

# if __name__ == '__main__':
#      n = int(input().strip())
#      for i in range(n+1):
#         arr = list(map(int, input().rstrip().split()))
#      print(" ".join(map(str,arr[::-1])))
n=int(input())
list=[]
for i in range(n+1):
    list.append((i))
print(list[::-1])   

# list comprehension

square=[i**2 for i in range(1,20) if i%2==0 ]
print(square)

# generator comprehension

square=(i**2 for i in range(1,20) if i%2==0 )
for num in square:
    print(num)
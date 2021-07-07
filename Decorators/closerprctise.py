def power(x):
    def cal_power(n):
        return n**x
    return cal_power
cube=power(3)
square=power(2)  
print(cube(4))
print(square(4))     

# Problem Statement

# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

# Take input as
# 1. Number of Interior walls
# 2. Number of Exterior walls
# 3. Surface Area of each Interior 4. Wall in units of square feet
# Surface Area of each Exterior Wall in units of square feet

# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

# Calculate and display the total cost of painting the property
# Example 1:

# 6
# 3
# 12.3
# 15.2
# 12.3
# 15.2
# 12.3
# 15.2
# 10.10
# 10.10
# 10.00
# Total estimated Cost : 1847.4 INR

# Note: Follow in input and output format as given in above example

interiar_wall=int(input())
exterial_wall=int(input())
int_wall=[]
ext_wall=[]
if interiar_wall:
    for i in range(interiar_wall):
        int_wall.append(float(input()))
if exterial_wall :
    for i in range(exterial_wall):
        ext_wall.append(float(input()))    
total=0        
for i in int_wall:
    c=i*18
    total+=c     
for i in ext_wall:
    c=i*12
    total+=c     
print(f"Total estimated Cost : {total} INR")

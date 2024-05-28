# Operators
# Logical "
age = 20 #variable
has_license = True #bool

# Check if the person is old enough to drive and has a license
if age >= 18 and has_license:
    print("You are allowed to drive.")
else:
    print("You are not allowed to drive.") 


a = 5
print(not(a>3 and a<10))

d = 7
print((d==7 or d < 3))

# Identity Operator->to compare memory locations
g = [1,2,3,4]
h =[5,6,7,8]
i =[1,2,3,4]

print(g is i)
print(g is h)
print(g==i)

m = g
print(m is g)
print(m is not g)

#Membership Operator->check element in an item
Letters =["a","b","c","d","z"]
if "y" not in Letters:
    print("hohoho")
if "z" in Letters:
    print("yes")
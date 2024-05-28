# count = 0  

# while count<=10:
#     print(count)    
#     count+=1

# num: int = 34

# name : str = 'Turing'


# Operators



#Wed Class 
person = {"name":'Gerald',
          'age':50}

print(type(person))
print(person.keys())
print(person.values())
print(person.items())

for key,value in person.items():
    print(key, value, sep=':')

#dictionary comprehension
#print isinstance()




### DATA TYPES







# NESTED LOOPS
ls=[[1,2,3,4],[11,12,13,14],[21,22,23,24]]

for i in range(len(ls)):
    for j in range(len(ls[i])):
        print(ls[i][j],end='')
    print()

for i in range(4):
    print(chr(94+1), end='')
    for j in range(1,5):# This loops repeats upto end time
        print(j, end='')
    print()


# REGEX
import re

text = 'Steve is our TM, he is 59 years old'

found = []
for letter in text:
    if letter ==' ':
        found.append(letter)
print(found)

matching = re.findall(r'[a-z]',text) #(r'>row string)
# metacharacters
# character classes-->[]
# predefined character classes
# \w - all alphanumeric characters
# \W - all non alphanumeric characters
# \d - any digit
# \D - any character that is not a digit
# \A - if a character exists at the beginning of a string
# \Z - if a character exists at the end of a string
# \s - 

print(matching)


# password 
# -length must be 8 characters
# -must contain a digit
# -must contain a capital letter
# -must contain a lowercase letter
# -must contain a special character

password = 'mysuperstrongpassword7'

if not re.findall(r'[0-9]',password):
    print('Password must contain a digit')
if not re.findall(r'[A-Z]',password):
    print('Password must contain an uppercase letter')
if not re.findall(r'[a-z]',password):
    print('Password must contain a lowercase letter')
if not re.findall(r'[⌃A-za-z0-9\s]',password):
    print('Password must contain a special character')


email = 'muligerald6@gmail.com'

res = re.match(r'[a-z{1}+[a-z0-9]{1,}+@[a-z0-9]{1,12}+\.+[a-z0-9]{1,}', email)

print(res)
#regex101

# 27th May 2024
# Constractor
# Template for defining  a product
class Product (): 

    Tally =  []  #>> supposed to print all the products
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        Product.Tally.append(self)


    def update_price(self, price): #>> supposed to add prices to the items
        self.price = price

        # Class Method
    def list_products(cls):
        return cls.Tally

    def __repr__(self) -> str:
        return f' <This product is {self.name}>' #>> prints the product name 
    
bread = Product('Bread', 65)
milk = Product('Milk', 60)


# Static method
def calculate_tax(price):
    return price*0.16

#Instance method
def total_plus_vat(self):
    return self.price+calculate_tax(self.price)


print(bread)
print(milk)

print(Product.Tally)
print(bread.price)
milk.update_price(100)
print(milk.price) 

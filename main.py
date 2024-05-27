# # count = 0  

# # while count<=10:
# #     print(count)    
# #     count+=1

# # num: int = 34

# # name : str = 'Turing'


# # Operators



# #Wed Class 
# person = {"name":'Gerald',
#           'age':50}

# print(type(person))
# print(person.keys())
# print(person.values())
# print(person.items())

# for key,value in person.items():
#     print(key, value, sep=':')

# #dictionary comprehension
# #print isinstance()




# # Data Types
# # Operators
# # Logical "
# age = 20 #variable
# has_license = True #bool

# # Check if the person is old enough to drive and has a license
# if age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.") 


# a = 5
# print(not(a>3 and a<10))

# d = 7
# print((d==7 or d < 3))

# # Identity Operator->to compare memory locations
# g = [1,2,3,4]
# h =[5,6,7,8]
# i =[1,2,3,4]

# print(g is i)
# print(g is h)
# print(g==i)

# m = g
# print(m is g)
# print(m is not g)

# #Membership Operator->check element in an item
# Letters =["a","b","c","d","z"]
# if "y" not in Letters:
#     print("hohoho")
# if "z" in Letters:
#     print("yes")

# #List-> store multiple items in a single variable
# #Ordered and changeable

# fruits = ['orange','lemon','mango','apple','banana']
# print(fruits[2])
# print(fruits[-1])
# print(fruits[1:3])#1 is included, #3 not included
# print(fruits[:4])#0,1,2,3

# # insert items
# matunda = ['orange','mango','apple','banana']
# matunda.insert(2,'lemon')
# print(matunda)

# #append function.....autimatically adds to the end of the list
# herufi = ['a', 'e','o','u']
# herufi.append('x')
# print(herufi)


# #extend list....add another list
# alphabets = [1,2,3,455]
# herufi = ['a', 'e','o','u']
# alphabets.extend(herufi)
# print (alphabets)

# #remove items
# herufi = ['a', 'e','o','u']
# herufi.remove('o')
# print(herufi)


# #empty the list
# herufi = ['a', 'e','o','u']
# herufi.clear()
# print(herufi)


# # Decorators
# def timed_greet(fn):
#     def wrapper(*args, **kwargs):
#         print('Good Morning!')
#         fn(*args, **kwargs)
#     return wrapper

# def greet_2():
#     print('Allan')

# # greet_2 = timed_greet(greet_2)#Decorator

# # greet_2()

# # @timed_greet()
# # def greet(name):
# #     print(name)

# # #greet = timed_greet(greet)

# # greet('Gerald')

# # def format_square(fn):
# #     def wrapper (*args, **kwargs):
# #         result = fn(*args, **kwargs)
# #         print(f'The square of {args[0]} is (result)')
# #     return wrapper


# # def square (number):
# #     return number*number

# # square(10)
# # # print (square(7))

# # NESTED LOOPS
# ls=[[1,2,3,4],[11,12,13,14],[21,22,23,24]]

# for i in range(len(ls)):
#     for j in range(len(ls[i])):
#         print(ls[i][j],end='')
#     print()

# for i in range(4):
#     print(chr(94+1), end='')
#     for j in range(1,5):# This loops repeats upto end time
#         print(j, end='')
#     print()


# # REGEX
# import re

# text = 'Steve is our TM, he is 59 years old'

# found = []
# for letter in text:
#     if letter ==' ':
#         found.append(letter)
# print(found)

# matching = re.findall(r'[a-z]',text) #(r'>row string)
# # metacharacters
# # character classes-->[]
# # predefined character classes
# # \w - all alphanumeric characters
# # \W - all non alphanumeric characters
# # \d - any digit
# # \D - any character that is not a digit
# # \A - if a character exists at the beginning of a string
# # \Z - if a character exists at the end of a string
# # \s - 

# print(matching)


# # password 
# # -length must be 8 characters
# # -must contain a digit
# # -must contain a capital letter
# # -must contain a lowercase letter
# # -must contain a special character

# password = 'mysuperstrongpassword7'

# if not re.findall(r'[0-9]',password):
#     print('Password must contain a digit')
# if not re.findall(r'[A-Z]',password):
#     print('Password must contain an uppercase letter')
# if not re.findall(r'[a-z]',password):
#     print('Password must contain a lowercase letter')
# if not re.findall(r'[⌃A-za-z0-9\s]',password):
#     print('Password must contain a special character')


# email = 'muligerald6@gmail.com'

# res = re.match(r'[a-z{1}+[a-z0-9]{1,}+@[a-z0-9]{1,12}+\.+[a-z0-9]{1,}', email)

# print(res)
# #regex101

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

    def __repr__(self) -> str:
        return f' <product {self.name}>' #>> prints the product name 
    
bread = Product('Bread', 65)
milk = Product('Milk', 60)

print(bread)
print(milk)

print(Product.Tally)
print(bread.price)
milk.update_price(100)
print(milk.price)




































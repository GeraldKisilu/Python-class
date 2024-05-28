#List-> store multiple items in a single variable
#Ordered and changeable

fruits = ['orange','lemon','mango','apple','banana']
print(fruits[2])
print(fruits[-1])
print(fruits[1:3])#1 is included, #3 not included
print(fruits[:4])#0,1,2,3

# insert items
matunda = ['orange','mango','apple','banana']
matunda.insert(2,'lemon')
print(matunda)

#append function.....autimatically adds to the end of the list
herufi = ['a', 'e','o','u']
herufi.append('x')
print(herufi)


#extend list....add another list
alphabets = [1,2,3,455]
herufi = ['a', 'e','o','u']
alphabets.extend(herufi)
print (alphabets)

#remove items
herufi = ['a', 'e','o','u']
herufi.remove('o')
print(herufi)


#empty the list
herufi = ['a', 'e','o','u']
herufi.clear()
print(herufi)
# to import a module
from math import *

print("=========================================== Numbers  ===========================================")
# define a variable 
x = 10

print(x)

print(max(5, 10))  # prints the maximum of two numbers
print(min(5, 10))  # prints the minimum of two numbers

print(abs(-7.25))  # prints the absolute value of a number

print(round(7.25))  # prints the rounded value of a number
print(round(7.75))  # prints the rounded value of a number

print(sqrt(64))  # prints the square root of a number

# define a string variable
print("=========================================== String Variable ===========================================")

name = "John Doe"

print(name)

# to access a character in the string

print(name[0])  # prints 'J'
print(name[1])  # prints 'o'

# to find the index of a character in the string
print(name.index('D'))  # prints 5

# when the character is not found, it raises a ValueError
# print(name.index('x'))  # raises ValueError: substring not found

# you can replace a character/string in the string
new_name = name.replace('J', 'X')

print(new_name)  # prints 'Xohn Doe'

new_name = name.replace('Doe', 'Smith')
print(new_name)  # prints 'John Smith'

# you can convert the string to upper case
upper_name = name.upper()
print(upper_name)  # prints 'JOHN DOE'

# you can convert the string to lower case
lower_name = name.lower()
print(lower_name)  # prints 'john doe'


# to convert number to string you can use str() function

print(type(str(125)))


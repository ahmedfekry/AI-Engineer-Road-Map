def sayHi(name, age):
    print("Hello, " + name + "!")
    print("Welcome to the Python world.")
    print("You are " + str(age) + " years old.")
    print("Have a great day!")


sayHi("Alice", 30)

# function with return value

def add(a, b):
    return a + b


#function with default parameter
def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

greet("Bob")  # uses default greeting
greet("Charlie", "Hi")  # uses custom greeting

greet(name="David", greeting="Welcome")  # using named arguments
greet(greeting="Good morning", name="Eve")  # using named arguments
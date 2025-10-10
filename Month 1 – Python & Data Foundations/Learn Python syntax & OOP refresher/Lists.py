# to defina a list of items
my_list = [1, 2, 3, 4, 5]

friends = ["Alice", "Bob", "Charlie"]

print(friends)

print(friends[0])  # prints 'Alice'
print(friends[1])  # prints 'Bob'
print(friends[2])  # prints 'Charlie'
print(friends[-1])  # prints 'Charlie'
# print(friends[8]) # raises IndexError: list index out of range  

# to change an item in the list
friends[0] = "Xavier"
print(friends)  # prints ['Xavier', 'Bob', 'Charlie']

# to append items to the list
friends.append("David")
print(friends)  # prints ['Xavier', 'Bob', 'Charlie', 'David']


# to insert intem to the list at a specific index
friends.insert(1, "Eve") # it will push the other items to the right
print(friends)  # prints ['Xavier', 'Eve', 'Bob', 'Charlie', 'David']

friends.insert(10, "Zara") # it will add the item at the end of the list note that 10 is out of range
print(friends)  # prints ['Xavier', 'Eve', 'Bob', 'Charlie', 'David', 'Zara']

# to remove an item from the list
friends.remove("Bob")
print(friends)  # prints ['Xavier', 'Eve', 'Charlie', 'David', 'Zara']

# to remove the last item from the list
friends.pop()
print(friends)  # prints ['Xavier', 'Eve', 'Charlie', 'David']

# to count the number of items in the list
print(len(friends))  # prints 4

# to sort the list
friends.sort()

print(friends)  # prints ['Charlie', 'David', 'Eve', 'Xavier']

# to count the occurrences of an item in the list
friends.append("Eve")
print(friends)  # prints ['Charlie', 'David', 'Eve', 'Xavier', 'Eve']
print(friends.count("Eve"))  # prints 2
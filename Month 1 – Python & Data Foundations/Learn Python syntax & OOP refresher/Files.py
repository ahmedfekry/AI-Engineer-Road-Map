# w mode overwrites the file if it exists
# a mode appends to the file if it exists
# r mode reads the file (default mode)

# to open a file in write mode
file = open("assets/example.txt", "w+")

# print(file.read())  # to read the file content

file.write("Adding a new line.")  # to write to the file

file.seek(0)  # to move the cursor to the beginning of the file

print(file.read())  # to read the file content again

# to close a file
file.close()
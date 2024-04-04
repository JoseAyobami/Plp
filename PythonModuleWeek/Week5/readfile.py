# Open a flie 
file = open("example.txt", "r")

# read the content of a file
content = file.read()

# print the file
print(content)

# closing the file 
file.close



# Writing a file

# Open a file

with open("example.txt", "w") as file:
    # write a file
 file.write("Hello World.\n")
 file.write("Hello world.\n")

file.close()

# OR

file = open("example.txt", "w")

file.write("Hello World.\n")
file.write("Open a file.\n")
file.cloed 

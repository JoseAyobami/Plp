""" words = ["one", "two", "three"] 
for x in words:
    print(x) 

# While loop
i = 10
while i < 20:
    print(i)
    i += 1 

names = ["Ayobami", "Abiola", "Ayoola", "Oladipupo", "Opeyemi", "Oluwafikunmi"]
for name in names:
    print("My other names is :", name)
    

 
Number = 500
while Number <= 1000:
    print("What is wrong here", Number)
    Number += 1


colors = ["red", "green", "blue", "white"]
color_i_want = "white"
for color in colors:
    if color == color_i_want:
        print("They have the color i want")
        break
    print(color)    


colors = ["red", "green", "blue", "white", "cream", "orange"]
color_i_want = "cream"
length = len(colors) # to know how many times we need to iterate based on the collection size
count = 0 # used to compare angainst length    
while count < length:
    print(colors[count])
    if colors[count] == color_i_want:
        print("They have the color i want!")
        break
    count += 1 """

    # Nested loop


groups = [["Ayobami", "Abiola", "Ayoola", "Oladipupo", "Opeyemi", "Oluwafikunmi"], ["red", "green", "blue", "white", "cream", "orange"]]
# this outer loop will iterate over each list in the gruop list
for group in groups:
    # this inner loop will will go through each name in each list
    for name in groups:
        print(name)
        
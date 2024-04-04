my_list = []

# Append element to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()

# sort my list in ascending order
my_list.sort()

index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)
print("Final list", my_list)
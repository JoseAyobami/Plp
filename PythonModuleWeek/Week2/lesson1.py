""" # List and Tuple 
list_a = [1, 2, 3, 4, 5] 
# index   0, 1, 2, 3, 4
list_a[2] = 45
list_a.append(6)
list_a.extend([7, 8])
list_a.pop(5)

for item in list_a:
  print(item) 

languages = ["Python", "Java", "C++", "Dart"]
# access index at 0
print(languages[-1])


my_list = ['a', 'c', 'd', 'f', 'v', 's', 'h']
# index     0,   1,   2,   3,    4,   5,  6
print(my_list[2:5])
print(my_list[5:])
print(my_list[:])
print(my_list[-3]) 

#Add Elements to a Python List

# 1. Using append
numbers = [21, 34, 65 ,53]
print("Before Append:", numbers)

numbers.append(40)
print("After Append:", numbers)


# 2 Using extend 

prime_numbers = [2, 3, 7]
print("list1:", prime_numbers)


even_numbers = [4, 6, 8]
print("list2:", even_numbers)

prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers) 


my_num1 = [1, 2, 3,]
print("list1:", my_num1) 

my_num2 = [4, 5, 6]
print("list2:", my_num2)

my_num1.extend(my_num2)
print("list3:", my_num1) 

# Remove an item from a list 
languages = ["Python", "Java", "Dart", "Swift"]
# index          0,      1,     2,       3
# index         -4,     -3,    -2,      -1
# del languages[1]
 # print(languages)

# del languages[-1]
# print(languages)

del languages[0 : 2]
print(languages) languages = ["Python", "Java", "Dart", "Swift"]

# using remove
languages = ["Python", "Java", "Dart", "Swift"]
languages.remove('Python')
print(languages)


languages = ["Python", "Java", "Dart", "Swift"]
for language in languages:
    print(language) 

# Python List Comprehension
numbers = [number*number for number in range (1, 6)]
print(numbers) 

# SET
# a set of integer type
student_id = {112, 113, 117, 119, 116, 115}
print("Student ID:", student_id)

# a set of string type
vowel_letters = {'a', 'e', 'o', 'u', 'i'}
print("Vowel Letters:", vowel_letters)  

# a set of mixed data
mixed_data = {'Hello', 2, 4.5, 'bye'}
print("Mixed data:", mixed_data )

# empty set
emptySet = set()
print(emptySet) 

# Add item in a set
numbers = {32, 67, 98, 65}
print('Initial set:', numbers)
 
 
# using add() method in a set
numbers.add(54)
print("Updated Set:", numbers) 

# using Updated() method
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = {'apple', 'google', 'microsoft'}

companies.update(tech_companies)
print(companies)

# using discard() method 
companies.discard('microsoft')
print(companies) 

# iterate for and while loop
fruits = {'Apple', 'Mango', 'Orange  '}

# for loop to access the fruits
for fruit in fruits:
    print(fruit)

 print(len(fruits))  

# first net
A = {1, 3, 5}

# second set
B =  {0, 2, 4}

# perform union operation using |
print('Union using:', A | B)

# perform union operation using union() method
print('Union using union():', A.union(B))   


# first net
A = {1, 3, 5}

# second set
B =  {1, 2, 3}

# perform intersection operation using &
print('Intersection using:', A & B)

# perform intersection operation using intersection() method
print('Intersection using intersection():', A.intersection(B)) 

 # first net
A = {2, 3, 5}

# second set
B =  {1, 2, 6}

# perform symmetric difference- operation using ^
print('using ^:', A ^ B)

# perform symetric difference operation using intersection ^ method
print(' symmetric difference using symmetric difference():', A.symmetric_difference(B)) 

# equal operation ==
A = {1, 3, 5}
B = {3, 5, 1, 4 }

if A == B:
    print('Set A and Set B are equal')

else:
    print('Set A and Set B are not equal')

    # DICTIONARY
    capital_city = {"Nepal": "Kathmandu", "England": "London"}
    print(capital_city)

    capital_city["Italy"] = "Rome"         # to add a new key or update a dictionary
    print("Updated Dictionary: ", capital_city)
   

    capital_city["Nepal"] = "New Zealand"  # to add a new value 
    print("Updated Dictionary: ", capital_city)
    print(capital_city["England"])   # to accesss a key 
del capital_city["Nepal"]            # to delete a key
print(capital_city)

print(capital_city.values()) 

# Membership Dictionary Test
Square = {1: 1, 3: 9, 4: 16, 6: 36}
print(1 in Square)
print(2  not in Square)
print(36 in Square)

# Iterating through a dictionary
Square = {1: 1, 3: 9, 4: 16, 6: 36}
for i in Square: 
    print(Square[i]) 


# STRING
# Access string Characters in Python
# We can acesss the the characters in three ways 
# 1. Indexing
greet = 'hello' 

# acess first index element
print(greet[1])  #'e'

# 2. Negative indexing
greet = 'hello' 

# acess first index element
print(greet[-4])  #'e'

# 3 Slicing
greet = 'hello' 

# acess character from 1st to 3rd index 
print(greet[1:4])  #'e'


message = 'Hola Amigos'
message ='H'
print(message) """

# Python Multiline String
message = """ 
Never gonna give up on you
Never gonna let you down

print(message) 


# Python String Operatoions

# 1. Compare Two Strings
str1 = "Hello, World"
str2 = "Ilove python"
str3 = "Hello, World"

# compare str1 and str2
print( str1 == str2)

# compare str1 and str3 
print(str1 == str3) """


# 2 Join Two or more Strings
greet = "Hello, "
name = "Jack"

# using + operator
result = greet  +  name
print(result)



# Data Types

num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3)) 

language = ["Kotlin", "Java", "JavaScript", "Flutter", "Python", "Dart"]

print(language)

print(language[0]) # Kotlin

print(language[3]) # Flutter

print(language[4]) # Python

language[1] = "Devops"

print(language)

print(language[1]) 

# Python Tuple Data 

product = ('Xbox', 499.99)
# create a tuple

# access the element at index 0
print(product[0])

# access the element at index 1
print(product[1])

product = ('Microsoft', 'Xbox', 499.99)

print(product[0])

print(product[1])

print(product[2])


# String Data Type

name = 'Python'
print(name)

message = 'Python for beginners'
print(message)


# Python Set Data Type

student_id = {112, 114, 116, 178,345}

# display student_id elements

print(student_id)

# display type of student_id

print(type(student_id))


# Dictionary Data Type
Captial_Country = {'Paris': 'France', 'Abuja': 'Nigeria', 'Singapore': 'Portugal', 'United kingdom': 'England'}

# create a dictionary named Capital_Country

print(Captial_Country)


# create a dictionary named Capital_Country
Captial_Country = {'Paris': 'France', 'Abuja': 'Nigeria', 'Singapore': 'Portugal', 'United kingdom': 'England'}

print(Captial_Country['Paris']) # print Paris

# print(Captial_Country['France']) # throws error message 


 
# Type Conversion

# declare and initialize two variables 

num1 = 6

num2 = 9

# print the output

print('This is the output')


# impicit Converting Integer to float

integer_number = 123

float_number = 1.23

new_number = integer_number + float_number 

# display new value and resulting data type

print("Value", new_number) 

print("Data type:", type(new_number)) 


# Explicit Conversion

num_string = '12'
num_integer = 13

print("Data type of num_string before typecasting:", type(num_string))


# explicit type conversion

num_string = int(num_string) 
print("Data type of num_string after typecasting:", type(num_string))

num_sum = num_integer + num_string
print("Sum", num_sum)
print("Data type of num_sum:", type(num_sum))
 








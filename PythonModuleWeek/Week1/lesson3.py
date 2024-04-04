# Basic Operator
# 1 Arithmetric Operators

a = 6
b = 4
# additon 
print('sum:', a + b)

# subtraction
print("substration:", a - b)

# Multiplication
print("Multiplication:", a * b)

#division
print('division:', a / b)

#floor division
print('floor division:', a // b) 

# modulo
print('modulo:', a % b)

# power
print('power;', a ** b) 

'''
# Assignment Operator
var x = 5

# ++ Op
a = 5
a += 1 # a = a + 1
print(a)
a -= 1 # a = a - 1
print(a)

a *= 2 # a = a * 2
print(a)

a /= 1 # a = a / 1
print(a)

a %= 4 # a = a / 4 
print(a)

a **= 3 # a = a ** 3
print(a)


# Assignment Exercise O
a = 20
b = 43
a += b # a = a + b
print(a) 

# Comparisons

a = 2
b = 3
print(a > b) 

a = 5
b = 6
print('a == b =', a == b) # equal to operator
print('a != b', a!= b) # not equal to operator
print('a <= b', a <= b) # less than or equal to operator 


# Logical Operators
a = 5
b = 6
print(a > 2) and (b >= 6) # True; i.e both are true

print(True and True) # True

print(True and False) # False

print(True or False) # True
print(False or False) # False
print(not True)
print(not False  )




# Special Character
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1) # prints False
print(x2 is y2) # prints True
print(x3 is y3) # prints True
print(x1 is x2) # prints False
print(x2 is not y2) # prints False


# Membership Operators
x = 'Hello World'
y = {1:'a', 2:'b'} # Check if the 'H' is present in x string
print('H' in x) # prints True

# check if 'hello' is present in x string

print('hello' not in x) # print true

# check if '1' key is present in y
print(1 in y)

# check if 'a' key is present in y
print('a' in y )


# Printing Output and User Input
print('Good morning!', end= ' ')
print('It is a rainy day')


print('Powerlp is ' +  'awesome. ')


# Python User Input
a = (1, 2, 3)
b = list(a)
print(b) 

a = 10
b = 3
print(a % b)

x={}
x[2] = 10
x[1] = [20, 30, 40]
print(x[1][2])
'''
name = 'Testing'
print(len(name))
# Creating a Pythagoras theorem
side_a = int(input('The width of the triangle is :'))
side_b = int(input('The height of the triangle is :'))
hypotenuse = (side_a ** 2 + pow(side_b, 2)) ** (1/2)
print('The hypotenuse is :',  round(hypotenuse, 2))
# local variable
'''def addNum(a, b) :
    # local variable declared inside a function
    sum = a + b
    return sum
# calling our function itn the print statement
print(addNum(43, 67))


def addNum (a, b):
    # local variable
    sum = a + b
    def double_it():
        # local variable
        double = sum * 2
        print(double)

    double_it() # calling our inner function  
    return sum
# calling our function inside print statement 
print(addNum (54, 100))    


globar_var = 3

def add_Num(a, b):
    total = a + b
    print("The Global_var is : ", globar_var)

    def double_it():
        double = total * 2
        print("The Global_var is : ", globar_var)
    double_it()
    return total
add_Num(12, 5) '''

def multiply_num(x, y):
    product = x * y

    def double_it():
        double = product ** 2
        print(double)
    double_it()
    return product
print(multiply_num (2, 6))
       
      

lara_olami = " Yes! LaraOlami is a good girl! "
def addNum(a, b):
    sum = a + b
    print("Is LaraOlami a good girl? ", lara_olami)

    def double_it():
        double = sum * 2
        print(double)
    double_it()
    return sum
addNum(12, 5)    


           
    

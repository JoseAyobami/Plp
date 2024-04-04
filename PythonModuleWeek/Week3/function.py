'''
def add_num():
    print(2 + 13)

    # calling a function
add_num()    


def addNum (a, b):
    answer = a + b
    return answer

# calling a function
total = addNum( 34, 56)
print("Total:", total)


def subNum (x, y):
    result = x - y
    return result

# calling a function
total = subNum( 345, 87)
print("Total:", total) '''

def add_Num(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
print("Total: ", add_Num(2,  5, 6, 7, 8, 13)) 


def addAges(**ages):
    sum = 0
    for k, v in ages.items():
        sum += v
    return sum
print("Total ages: ", addAges(Ayobami=25, Jose=25, Abiola=25, Oladipupo=25))



     


def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else: 
        return False

print(large_power(10, 6))
print(large_power(2, 15))

def division_num(num):
    if num %  10 == 0:
        return True
    else: 
        return False

print(division_num(50))
print(division_num(7,))    
        
       
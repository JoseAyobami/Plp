# POLYMORPHISM Built in function len()
#student = ['kelly', 'john', 'Dave']
#School = ('ABC AND')
#print(len(student))
#print(len(School))

# POLYMORPHISM with INHERITANCE
# METHOD OVVERIDING
'''class Vehicle:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price
    def show(self):
        print('Details:', self.name, self.color, self.price)   
    def max_speed(self):
        print('Vehicle max speed is 150')
    def change_gear(self):
        print('Vehicle change 6 gear')

# inherit from Vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car speed is 240')
    def change_gear(self):
        print('Car change 7 gear')


# object Car
car = Car('Car X1', 'Red', 20000)
car.show()
car.max_speed()
car.change_gear()


# object vehicle
vehicle = Vehicle('Truck X1', 'Blue', 10000)
vehicle.show()
vehicle.max_speed()
vehicle.change_gear() 


# Override Built in function                  
class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')

        count = len (self.basket)   
        # count total items in a different way
        # pair of shoes and shirt+pant  
        return count * 2 
shopping = Shopping(['Shoes', 'dress'], 'Jessica')
print(len(shopping))        

# Polymorphism in class method

class Ferari:
    def fuel_type(self):
        print('Petrol')

    def max_speed(self):
        print('Max speed is 250')

class BMW:
    def fuel_type(self):
        print('Diesel')
    def max_speed(self):
        print('Max speed is 240')

ferari = Ferari()
bmw = BMW()

# iterate object of the same type
for car in (ferari, bmw):

# call methods without checking class of object
 car.fuel_type()
 car.max_speed()  '''


# Polymorphism with Function and Object
class Ferari:
    def fuel_type(self):
        print('Petrol')

    def max_speed(self):
        print('Max speed is 250')

class BMW:
    def fuel_type(self):
        print('Diesel')
    def max_speed(self):
        print('Max speed is 240')

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferari()
bmw = BMW()

car_details(ferrari)   
car_details(bmw) 
                  
                    
        
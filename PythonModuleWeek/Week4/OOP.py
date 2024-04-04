# CLASS
'''
class Vehicle:
    def __init__(self, make, model, year):
        # declaring attribute
        self.make = make
        self.model = model
        self.year = year
# definig functions
    def start(self):
        raise NotImplementedError("Subclass must implement thsis abstract method ")

    def stop(self):
        raise NotImplementedError("Subclass must implement this method")

class Car(Vehicle):
    def start(self):
            return f"The {self.year} {self.make} {self.model} start"
    def stop(self):
            return f"The {self.year} {self.make} {self.model} stop"   
class Motorcycle(Vehicle):
    def start(self):
            return f"The {self.year} {self.make} {self.model} revs the engine and starts"
    def stop(self):
            return f"The {self.year} {self.make} {self.model} applies the brake and stop"     

# creating instances of car and Motorcycle

my_car = Car("Toyota", "Camry", 2020)
my_motorcycle = Motorcycle("Honda", "sobdg", 2019)

    # using the start and stop methods without needing to know the internal implementation
print(my_car.start())
print(my_car.stop())
print(my_motorcycle.start())
print(my_motorcycle.stop())    

#Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# class, object, Encapsulation
class Circle(Shape):
    def __init__(self, radius):
        self. __radius = radius # Encapsulated attribute
    def area(self):
        return 3.14 * self.__radius * self.__radius

# inheritance
class Square(Shape):
    def __init__(self, side):
        self.__side = side # Encapsulated attribute
    def area(self):
        return self.__side * self.__side

# Polymorphism
def print_area(shape):
    print("Area: ", shape.area())

    # create objects and demonstrate polymorphism
circle = Circle(5)
square = Square(4) 
print_area(circle) # output: Area: 78.5
print_area(square) # output: Area: 16          



class Employee:
    def __init__(self, name, age, ID_number, department):
        self.name = name
        self.age = age
        self.ID_number = ID_number         
        self.department = department

    def display_employee_details(self):
      print(f"Name: {self.name}") 
      print(f"Age: {self.age}")
      print(f"ID_number: {self.ID_number}")
      print(f"Department: {self.department}")

emp = Employee("Jose", 30, "F234", "Software Engineering")
emp.display_employee_details()         

# CLASS 
class Person:
    nationality = 'Nigeria'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayinfo(self): 
        print(f'Person name: {self.name}')  
        print(f'Age: {self.age}')  

person = Person('Jose', '25')
person.displayinfo()      

# INHERITANCE
class Vehicle:
    def vehicle_info(self):
        print('Inside Parent (Vehicle) class')

# Child class
class Car(Vehicle):
    def car_info(self):
        print('Inside Child (Car) class')

#W craete an object
car = Car()

#acess vehicle's info using car object
car.vehicle_info()
car.car_info() 


# Parent class
class Vehicle:
    def vehicle_info(self):
        print('This is Parent(Vehicle) class')

# child class
class Car(Vehicle):
    def car_info(self):
        print('This is Child (Vehicle) class')

# create an object
car = Car()

# access vehicle' info using car object
car.vehicle_info()
car.car_info() 


# Creating class in python

class MySelf:
    def __init__(self, name, age, hobby, color, favorite_food, dream, goals, vision):
        self.name = name
        self.age  = age
        self.hobby = hobby
        self.color = color
        self.favorite_food = favorite_food
        self.dream = dream
        self.goals = goals
        self.vision = vision
    def display_myself_info(self):
        print(f"Name:  {self.name}") 
        print(f"Age:  {self.age}")
        print(f"Hobby:  {self.hobby}")
        print(f"Color:  {self.color}") 
        print(f'Favorite food:  {self.favorite_food}')
        print(f"Dream:  {self.dream}")
        print(f"Goals:  {self.goals}")
        print(f"Vision:  {self.vision}")

myself = MySelf('Jose Ayobami', 1000, 'Watching Movies i repeat watching movies', 'White and Black', 'Amala dudu pelu eni soup toni eran ogufe', 'Just to be sleeping in future', 'Sleeping ni seh madami lamu', 'Playing games tho')
myself.display_myself_info()        

# Parent ckass
class Love:
    def love_info(self):
        print('Swrs I am in love')

class Movies(Love):
    def my_movies_info(self):
        print("All movies")

films = Movies()

films.love_info()
films.my_movies_info()        

            

# Parent class
class Person:
    def person_info(self, name, age):
        print('Inside person class')
        print('Name:', name, 'Age:', age)

class Company:
    def company_info(self, company_name, location):
        print('Inside company class')
        print('Company Name:', company_name, 'location:', location)



class Employee(Person,  Company):
    def employee_info(self, salary, skill):
        print('Inside Empoyee class')
        print('Salary:', salary, 'Skill:', skill)

 # acess 
emp = Employee()
emp.person_info('Jose', 45)
emp.company_info('Amazon', 'UK')  
emp.employee_info('$5000', 'Programmer') '''     

# hierarchical inheritance
class Vehicle:
    def info(self):
        print('This is a vehicle')


class Car(Vehicle):
    def car_info(self, name):
        print('Car name is', name)

class Truck(Vehicle):
    def truck_info(self, name):
        print('Truck name is', name)


obj1 = Car()
obj1.info()
obj1.car_info('Benz')


obj2 = Truck()
obj2.info()
obj2.truck_info('Tesla')

# hybrid inheritance
class Vehicle:
    def vehicle_info(self):
        print('Inside the vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('Inside Car class')


class Truck(Vehicle):
    def truck_info(self):
        print('Imside the Truck class')

class SportCar(Car, Truck):
    def sport_car_info(self):
        print('Imside SportCar class')

s_car = SportCar()
s_car.vehicle_info() 
s_car.car_info()
s_car.sport_car_info()

# Python Super Function
class Company:
    def company_name(self):
        return 'Google'

class Empolyee(Company):
    def info(self):
        c_name = super() .company_name()
        print('Jessica works at', c_name)

emp = Empolyee()
emp.info()

class Company:
    def fun1(self):
        print('Inside Parent class')
class Employee(Company):
    def fun2(self):
        print('Inside Child class')
class Player:
    def fun3(self):        
        print('Inside Player class')

print(issubclass(Employee, Company))
print(issubclass(Player, Company))
                
                    
                                           
                                  
                        
                    
            
'''class MyClass:
    def __init__(self, name): # constructor
        self.name = name

    # creating an instance of myclass
obj = MyClass("Jose")
del obj
print(obj.name) 

# Base/Super/Parent
# Single Inheritance
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle") '''

# Single inheritance
# Base/Super/Parent class
class Vehicle:
    def __init__(self, name, sound,):
        self.name = name
        self.sound = sound

    #method
    def make_sound(self):
        print(f"{self.name} make {self.sound} sound")
# Subclass/ Child class
class Car(Vehicle):
    def __init__(self, name, sound, year ):
        super().__init__(name, sound)     
        self.year = year  
        # method    
    def run_fast(self): 
        print(f"{self.name} run faster than anything and was made in the year {self.year} ")  

#  creating an instance of an object
car = Car("Benz", "poof", 2024)
car.make_sound()
car.run_fast()             

class School:
    def __init__(self, name, college, matricNo, cgpa):
        self.name = name
        self.college = college
        self.matricNo = matricNo
        self.cgpa = cgpa


        #mathod
    def displayInfo(self):
        print(f"{self.name} in {self.college} with {self.matricNo} is on {self.cgpa} grade ")

# Child / Subclass
class Student(School):
    def __init__(self, name, college, matricNo, cgpa, studentName, dept ):
        super().__init__(name, college, matricNo, cgpa)
        self.studentName = studentName
        self.dept = dept

    def student_info(self):
        print(f"{self.studentName} go to {self.name} and is in {self.dept} with {self.cgpa} grade ")


# create an instance of the object
student = Student("Funnab", "BioScience", 20180567, 2.50, "Python", "Bch")    
student.displayInfo()
student.student_info()               
           
           
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        

def login(self):
    print(f"{self.username} logged in")

def logout(self):
    print(f"{self.username} looged out")


class Customers(User):
    def __init__(self, username, email, cart=[]):
        super().__init__(username, email)
        self.cart = cart

    # method
    def purchase(self, item):
        self.cart.append(item)
        print(f"{self.username} purchased (item)")    

class Admin(User):
    def __init__(self, username, email, permission=[] ):
        super().__init__(username, email,) 
        self.permission = permission


    # method
    def create_user(self, username, email):
        print(f"{self.username} created user {username}")

customer = Customers("Jose", "ayenijoseph45@gmail.com", 3 )
admin = Admin("Ayobami", "ayenijoseph45@gmail.com", 6)
customer.purchase()
admin.create_user()


class Transaction:
    def __init__(self, amount, timestamp):
        self.amount = amount
        self.timestamp = timestamp
        
        

    # Method
    def process(self):
        print(f"Transaction processed at {self.timestamp}")


class Deposit(Transaction):
    def __init__(self, amount, timestamp, source_account):
        super().__init__(amount, timestamp, source_account)
        self.sources_account = source_account

     # Method    
    def confirm_deposit(self):
        print(f" Confirmed deposit from {self.source_account}")

class Withdrawal(Transaction):
    def __init__(self, amount, timestamp, destination_account):
        super().__init__(amount, timestamp, destination_account)
        self.destination_account = destination_account

    # Method
    def verify_withdrawal(self):
        print(f"Withdrwal verified for {self.destination_account}")
        
              
                       


           
        
               
    

                     
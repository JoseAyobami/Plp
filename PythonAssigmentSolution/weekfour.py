class Person:
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"Name of the Person:, {self.name}")
        print(f"Age of the Person:, {self.age}") 
        print(f"Gender of the Person: {self.gender}") 


introduce = Person("Jose", 25, "Male")
introduce.display_info()           
'''class Workout:
    def __init__(self, exercise_type, duration, calories_burned):
        self.excercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned


    # override the built-in print function to display workout details
    def __str__(self):
        return f"Exercise Type: {self.excercise_type}\nDuration: {self.duration} minutes\ncalories Burned {self.calories_burned}"
    # create some workout object
workout1 = Workout('Runnig', 30, 250)
workout2 = Workout('Strength Training', 45, 300)

    #print out the workout details using the overridden __str__ method
print(workout1)
print(workout2) '''

class Animals:
    def __init__(self, name):
        self.name = name
    # define a method
    def makeSound(self):
        print("animal noise")

class Bird:
    def __init__(self, name, sound):
        self.name = name
    # define a method
    def makeSound(self):
        print("animal    noise")

class Lion(Animals):
    def lion_sound(self):
        print("Roar")


class Zebra(Animals):
    def zebra_sound(self):
        print("Neigh")

class Parrot(Bird):
    def parrot_bird(self):
        print("Caw")


# create an object
animal = Animals()
                         
        
        
               
            

         
        
         
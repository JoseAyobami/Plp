/*class Cat {
  // Properties
  String color;
  String breed;

// constructor
  Cat(this.color, this.breed);

// method/ function/ behaviour
  void play() {
    print('This cat palys too much');
  }

  void smart() {
    print('This cat is way smarter than any thing');
  }
}

void main() {
  // create an instance of the object
  var myCat = Cat("Blue", "Labrador");

  // Accessing the properties
  print("Color: ${myCat.color}");
  print("Breed: ${myCat.breed}");

  myCat.play();
  myCat.smart();
} 

//The challenge is to create a program that has the following features:

//An object-oriented model that uses classes and inheritance
//A class that implements an interface
//A class that overrides an inherited method
//An instance of a class that is initialized with data from a file
//A method that demonstrates the use of a loop

class Student {
  // properties
  late String name;
  late String age;
  late String dept;
  late String grade;
  // function to display the properties
  void display() {
    print('$name');
    print('$age');
    print('$dept');
    print('$grade');
  }
}

void main() {
  // create an instances to acess the properties
  var myStudent = Student();
  myStudent.name = 'Tope';
  myStudent.age = '45';
  myStudent.dept = 'Bch';
  myStudent.grade = 'First class';
  myStudent.display();
} */

class Instructor {
  // properties
  String name;
  int phonenumber;
  bool isMarried;
  int age;
  String country;
  String hobby;

  // constructor = parametric contructor
  Instructor(this.name, this.phonenumber, this.isMarried, this.age,
      this.country, this.hobby);

  void dispalyInfo() {
    print('Name: $name');
    print('Phone Number: $phonenumber');
    print('Is Married ${isMarried ? 'Married' : 'Single'}');
    print('Age: $age');
    print('Country: $country');
    print('Hobby : $hobby');
  }
}

// main function to create the object
void main() {
  var myInstructor = Instructor("Dennis", 07034475242, true, 45, 'Nigeria',
      'Watching movies and Traveling');
  // call the function
  myInstructor.dispalyInfo();
}

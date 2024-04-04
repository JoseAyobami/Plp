/*class Dog {
  // properties
  String breed;
  String color;


  // constructor
  Dog(this.breed, this.color);

  // methods 
  void bark() {
    print("Woof");
  }

void run () {
  print("The dog is runnig.");
}

}

void main () {
  // creating an instance of the Dog class/object
  var myDog = Dog('Labrador', 'Golden');

  // Accessing properties
  print('Breed: ${myDog.breed}');
  print('color: ${myDog.color}');

  // calling the methods
  myDog.bark();
  myDog.run(); 
} 

class Student{
  // properties
  String name;
  String age;

// constructor
Student(this.name, this.age);

// method
void excellent () {
  print("This set of student are in excellent grade");
}
void average () {
  print("This groups of student are in average grade");
}

}

void main () {
  // create an instance of the student class. myStudent is the instance of the class
  var myStudent = Student("Jose", "25");

  // Acessing the properties/attributes
  print('Name: ${myStudent.name}');
  print('Age: ${myStudent.age}');

  // calling the method
  myStudent.excellent();
  myStudent.average();

} 


class Person {

  //properties
String origin;
String country;

//constructor
Person(this.origin, this.country);

// methods
void character () {
  print('Good');
}

void hobby () {
  print('Reading');
}
}

void main () {
  // create an instance of the class Person
  var thePerson = Person('Yoruba', 'Nigeria');

  // Accessing the properties
  print('Origin: ${thePerson.origin}');
  print('Country: ${thePerson.country}');

  // calling the methods
  thePerson.character();
  thePerson.hobby(); 
} 

class Person {
  // Properties of the class Person
  late String name;
  late String age;
  late String dept;

  // function to display the properties

  void display() {
    print('$name');
    print('$age');
    print('$dept');
  }
}

void main() {
  // object to access the properties of the class
  var person = Person();
  person.name = 'Jose';
  person.age = '25';
  person.dept = 'Software Engineering';
  person.display();
} 

// Multiple constructor
class Rectangle {
  // Properties
  int width;
  int height;
  // first constructor
  Rectangle(this.width, this.height);

  

  // second constructor
  Rectangle.square(int size) {
    width = size;
    height = size;
    
  }
}

main() {
  final rect = Rectangle(3, 4);

  final square = Rectangle.square(10);
  rect.width();
  rect.height();
  Rectangle.square();
} */


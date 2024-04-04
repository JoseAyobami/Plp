/*class Rectangle {
  // properties
  final int width;
  final int height;

  // Unnamed constructor
  Rectangle(this.width, this.height);

  // named constructor
  Rectangle.square(int size) : this(size, size); // create a square

  // method to calculate area
  int getArea() {
    return width * height;
  }

  // method to calculate perimeter
  int getPerimeter() {
    return 2 * (width + height);
  }

  // check if it is a square (optional)
  bool get isSquare => width == height;
}

void main() {
  // Rectangle with width 3 and height 4
  var rectangle1 = Rectangle(3, 4);

  // square with size 10
  var square = Rectangle.square(10);

  // Accessing properties and mwthod
  print("Rectangle area: ${rectangle1.getArea()}");
  print("Rectangle Perimeter: ${rectangle1.getPerimeter()}");

  // using square property

  if (square.isSquare) {
    print("This is square with side ${square.width}");
  } else {
    print("Square area: ${square.getArea()}");
  }
}

class Person {

  String _name;
  Person(this._name);
  String get name {
    return _name.toUpperCase();
  }
}

void main() {
  // object creation
  final person = Person('Bob');
  // Accessing the property
  print(person.name);
}  

class Person {
  String _name;
  Person(this._name);

  set name(String newName) {
    _name = newName.toUpperCase();
  }
}

void main() {
  // object creation
  final person = Person('Bob');
  person.name = 'Alice';
  print(person._name);
} 

class Person {
  //private field to store the name
  String _name;

  //constructor to initialize the name
  Person(String name) {
    _name = name.toUpperCase(); // Ensure uppercase name on creation
  }
  // Getter to access the name in uppercase
  String get name {
    return _name;
  }

  // setter to modify th name (enforces uppercse)
  set name(String newName) {
    _name = newName.toUpperCase(); //convert to uppercase before assigning
  }
}

void main() {
  final person = Person('Bob');
  person.name = 'Alice'; // set name to 'Alice'
  print(person.name); // pritn 'ALICE'
} */

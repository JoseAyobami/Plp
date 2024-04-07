// Define an interface

abstract class MakeSound {
  void makeSound();
}
// Class reprensenting an Animal (inherits from MakeSound)
class Animal implements MakeSound {
  String name;
  Animal(this.name);
  @override
  void makeSound() {
    print('The $name makes a generic sound.');
  }

}
// class representing a dog (inherit from animal)
class Dog extends Animal {
  Dog(String name) : super (name);
  // override makeSound to provide a specific sound for Dog
  @override
  void makeSound() {
    print('The $name barks!');
  }

}

// function to read data from a file (replace with actual file reading logic)
String readFile (String filePath) {
  // simulate reading data from a file
  return "Fido";
}

void main () {
  // Read animal name from a file (replace with actual filepath)
  String animalName = readFile ("animal_name.txt");
  // create a Dog object with the name read from the file
  Animal animal = Dog(animalName);

  // Loop to make the animal sound 3 times
  for (int i = 0; i < 3; i++) {
    animal.makeSound();
  }
}
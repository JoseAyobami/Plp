/* // Abstraction

abstract class Animals {
  // property
  int legs = 0;
  // method;
  void makeSound();
}

class Cat extends Animals {
  @override
  void makeSound() {
    print("Meow");
  }
}

void main() {
  Cat myCat = Cat();
  myCat.makeSound();
} */

abstract class SubjectMathematics {
  // method
  void studentPerformance(int grade) {}
  void StudentConduct(String message) {}
}

class Student extends SubjectMathematics {
  Student(String? studentName, String? admissionNumber);
  @override
  void studentPerformance(int grade) {
    if (grade > 50) {
      print("PASS");
    } else {
      print("FAIL");
    }
  }

  @override
  void StudentConduct(String message) {
    if (message == 'good') {
      print("GOOD STUDENT");
    } else {
      print("DO SOMETHING");
    }
  }
}

void main() {
  Student myStudent = Student('Bliss', '1781');
  myStudent.studentPerformance(45);
}

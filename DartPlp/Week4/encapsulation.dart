/* //Abstraction

abstract class Animals {
  // property
  String name = 'Halogen';
  String family = 'Invertebrate';

  // method
  void typeofWalk();
}

class Monkey extends Animals {
  @override
  void typeofWalk() {
    print('Flying');
  }
}

void main() {
  Monkey myMonkey = Monkey();
  myMonkey.typeofWalk();
}*/

abstract class SubjectMathematics {
  // property imbibe in method
  void studentPerformance(int grade) {}
  void studentConduct(String message) {}
}

// inheritance
class Student extends SubjectMathematics {
  Student(String? studentName, String? studentDept);

  @override
  void studentPerformance(int grade) {
    if (grade < 50) {
      print(' AVERAGE');
    } else {
      print('PASS');
    }
  }

  @override
  void studentConduct(String message) {
    if (message == 'good') {
      print('GOOD STUDENT');
    } else {
      print('NOT GOOD');
    }
  }
}

void main() {
  // object creation
  Student isStudent = Student('Prudence', 'Engineering');
  isStudent.studentPerformance(70);
}

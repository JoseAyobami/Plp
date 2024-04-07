// CLASS 1
class Teacher{

  // Teacher Property/Field
  String name;
  int age;
  String subjectTeach;

  // Constructor
  Teacher(this.name, this.age, this.subjectTeach);

  // Method that print out Teacher's Information
  void displayTeacherInfo(){
    print('Nmae of Teacher: $name');
    print('Age: $age');
    print('Subject teach by the Teacher: $subjectTeach \n');
  }

}

// CLASS 2
class Student{
  
  // Student Property/Field
  String name;
  int age;
  String gradeLevel;

  // constructor
  Student(this.name, this.age, this.gradeLevel);

  // Method that print out Student' Information
  void displayStudentInfo(){
    print('Name of Student: $name ');
    print('Student Age: $age');
    print('Student Grade: $gradeLevel');

  }

}

void main () {

  // Creating an instance of object for class 1
  Teacher myTeacher = Teacher('Mr Ayobami', 35, 'Dart Programming Language');

  // printing out
  myTeacher.displayTeacherInfo();
  
  // Creating an instance of object for class 2
  Student thisStudent = Student('Jose', 25, 'Second Class Upper');

  // printing out 
  thisStudent.displayStudentInfo();

}

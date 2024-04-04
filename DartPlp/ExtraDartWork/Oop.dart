// declaring class with paramete 

class School {

  // properties
  String nameofSchool;
  int numberofAwardWon;
  String location;
  double sizeofLandMass;

  // constructor
  School(this.nameofSchool, this.numberofAwardWon, this.location, this.sizeofLandMass);

  // methods/bahaviors
  void characteristicsofSchool () {
    print('Good at academics');
    print('Good at sport');
    print('Bad at Debate');
    
}

void teacherAssitance () {
  print('The teacher assist is excellent');
  print('The teacher assist is good');
  print('The teacher assist is poor');
  
}

}

void main () {
 

  // creating an instance of the class/object
var mySchool = School('ALT School', 10, 'Nigeria', 5000);

  // Accessin through the method

  print('Name of School: ${mySchool.nameofSchool}');
  print('Number of Award Won: ${mySchool.numberofAwardWon}');
  print('Location: ${mySchool.location}');
  print('The size of land Mass: ${mySchool.sizeofLandMass}');
  

// calling a method
mySchool.characteristicsofSchool();
mySchool.teacherAssitance();


}







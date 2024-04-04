// if-else condition
void main () {
  int grade = 80;
  String  result;
  if (grade >= 80) {
    result = 'Excellent';
  } else if (grade >= 80) {
    result = 'Very good'; 
    
    } else {
      result = 'Needs improvement';

    } 
    print(result);


// Switch statements


  String day = 'Tuesday';
  String activity;
  switch (day) {
    case 'Monday':
      activity = 'Planning';
      break;
    case 'Tuesday':
    case 'Wednesday':
      activity = 'Coding';
      break;
      default:
      activity = 'Relaxing';

print(activity);        
  


// for loop

  for (int i = 1; i <=5; i++) {
  print('Iteration');

 

// for in loop for iterating elements

  List <String> fruits = ['apple', 'banana', 'orange'];
  for (String fruit in fruits) {
    print(fruit);
  }




// while loop executes code as long as a condition is true


  int count = 0;
while (count < 3) {
  print('Count: $count');
  count++;
  

 

// Jump Statement

  for (int i = 1; i <= 10; i++) {
    if (i == 5) {
      break; // exit after printing 4
    }
    print(i);
  }

  int number = 10;
print("Enter number: ");
if (number >= 10){
  print("Your number is greater than 10");
} else if (number <= 10) {
  print("Your number is less than 10");
}
else if(number == 10) {
  print("Your is equal to 10");
}
else {
  print("Your number is out of range");
}
}

}
  }
}
/*void main(){
  var age = 10;
  if (age > 18){
    print('I am nice person');
  }
  else if (age == 18){
    print('I am a voter');

  } else {
    print('Damn');
  }
  } 
  void main(){
    int i = 5;
    switch(i) {
      case 1:
      print('The value is 1');
      break;
      case 2:
      print('The value is 2');
      break;
      case 3:
      print('The value is 3');
      break;
      default:
      print('The value is out of range');
      break;
    }
  }
  */


import 'dart:io';

void main () {
  print('Enter number');
  int num = int.parse(stdin.readLineSync()!);
  if (num % 2 == 0) {
    print("$num is an even number");
  } else {
    print("$num is an odd number");
  }

bool isprime(int n) {
  if (n <= 1) {
    return false;
  }
  // iterate through numbers from 2
  for (int i = 2; i <= n / 2; i++) {
    if (n % i == 0){
      return false;
    }
    
  }
  return true;
}

if (isprime(num)){
  print("$num is prime");
} else {
  print("$num is not prime");
}

}



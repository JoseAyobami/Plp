import 'dart:io';
void main () {
  while(true){
    try{
      print('Enter the first numbers:');
var num1 = num.parse(stdin.readLineSync()!);

print('Enter the second number:');
var num2 = num.parse(stdin.readLineSync()!);
print('\nThe sum of (num1 and num2): ${num1 + num2}');

      break;
    } on FormatException{
      print('Invalid Value');
    } catch(e){
      print('Invalid Value');
    }
  }
  
}

int addNum(num1, num2) {
  return num1 + num2; 
}
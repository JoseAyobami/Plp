/*
// writing function outside main function
void printName() {
  print("My name John James");
}
 void main(){
  print('My name is Jose'); 
  printName(); 
 } 


 void addNum(num1, num2){
  num sum = num1 + num2;
    print("The sum is $sum");
 }
 void main(){
  addNum(10, 20);

 } 


// parameter and return type
int add(int a, int b) {
  var total;
  total = a + b;
  return total;
}
void mul(int a, int b) {
  var total;
  total = a * b;
  print("Multiplication is : $total");

} */


import 'dart:io';

void main () {
  String? details () {
    print("Enter your name");
    String? name = stdin.readLineSync()!;
    print('Enter your age:');
    int age = int.parse(stdin.readLineSync()!);
    print("Enter your country:");
    String? country = stdin.readLineSync()!;
    return ("I am $name age $age country $country");
  }
  print(details());
} 
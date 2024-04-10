// A  dart program that 

import 'dart:io';

void main () {
  while(true){
    try{
      print('Enter number');
  var Num1 = num.parse(stdin.readLineSync()!);
  if (Num1 % 2 == 0){
    print('The number you input is an even Number.');

  } else if(Num1 % 2 == 1){
    print('The number you input is an odd number');
  } else{
    print('This number is out of range');
  }
      break;
    } on FormatException catch(e){
      print('Error: Invalid format - ${e.message}');
    } catch(e){
      print('Error: ${e.toString()}');

    }
  }

}
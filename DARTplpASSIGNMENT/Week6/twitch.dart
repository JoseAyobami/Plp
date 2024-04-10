import 'dart:io';

void main () {
  try{
    stdout.write('Enter a String Value: ');
    String? input = stdin.readLineSync();

    if (input == null) {
      throw FormatException('No input provided.');
    }



  switch (input) {
    case 'jose':
    print('My name is Jose');
    break;

    case 'ayobami':
    print('My other name is Ayobami');
    break;

    case 'Plp':
    print('PLP is a good tech bootcamp and their teachers are sounded very well');
    break;
    case 'dart':
    print('Dart is beautiful but heavy programming language to learn');
    break;
    default:
    print('Such a beautiful learning');
    break;

  }

  } catch (e) {
    print('Error: $e');

  } 
} 
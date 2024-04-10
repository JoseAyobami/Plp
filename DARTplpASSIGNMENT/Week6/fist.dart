import 'dart:io';

void main (){
  stdout.write('Enter a list of numbers seperated by space: ');

  // Reading input from the user
  String input = stdin.readLineSync()!;

  // Splitting thr input string into a list of strings
  List <String> numbersAsString = input.split(' ');

  // Converting the list of strings to a list of integers
  List <int> numbers =numbersAsString.map(int.parse).toList();

  // Finding the largest number in the List
  int? largestNumber = findLargestNumber(numbers);

  if(largestNumber != null) {
    print('The largest number in the list: $largestNumber');
  } else{
    print('No valid numbers were entered.');
  }
  

} 

int? findLargestNumber(List<int> numbers) {
  if(numbers.isEmpty) {
    return null;
  }

  int largest = numbers[0];
  for(int number in numbers) {
    if(number> largest) {
      largest = number;
    }
  }

  return largest;
}
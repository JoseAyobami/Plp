// Creating a function that get the first element
dynamic getFirstElement(List list) {
if (list.isEmpty) {
  return null;
}
return list[0];
}

void main (){
  // calling the function
  List colors = ["Red", "Blue", "Orange",];
  dynamic firstColor = getFirstElement(colors);
  // printing the output: The first color in the is : Red
  print("The first color in the list is : $firstColor");

}
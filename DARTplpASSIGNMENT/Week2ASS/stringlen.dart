// creating a function to get a string length
int stringLength(String str) {
  return str.length;
}

void main(){
  String name = "Ayobami";
  int nameLength = stringLength(name);
  print("The length of the string 'Ayobami' is : $nameLength");
}

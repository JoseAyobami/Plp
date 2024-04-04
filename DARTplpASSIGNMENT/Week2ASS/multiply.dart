// Creating a function that multiply two numbers
int multiplyTwo (int m, int n) {
  int product = m * n;
  // returning the value
  return product;
}

void main (){
  // Calling the function
  int product = multiplyTwo(17, 54);
  // printing the output; the product of 17 and 54 is; 918
  print("The product of 17 and 54 is : $product");
}
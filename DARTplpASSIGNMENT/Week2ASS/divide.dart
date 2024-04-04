// Creating a function that divide two numbers
num divideTwo (double a, double b) {
  num quotient = a / b;
  // returning the rsult
  return quotient;
}

void main (){
  // Calling the function
  num qoutient = divideTwo(100.0, 25.0);
// printing the output: the division of 100.0 and 25.0 is 4.0
print("The division of 100.0 and 25.0 is : $qoutient");

}
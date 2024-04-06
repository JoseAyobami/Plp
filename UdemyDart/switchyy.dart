/* void main() {
  var x = 5;
  var y = 3;
  var op = 'j';
  switch (op) {
    case '+':
      print('x + y = ${x + y}');
      break;

    case '*':
      print('x * y = ${x * y}');
      break;

    case '-':
      print('x - y = ${x - y}');
      break;

    case '/':
      print('x / y = ${x / y}');
      break;
    case '%':
      print('x % y = ${x % y}');
      break;
    default:
      print("Not valid!");
      break;
  }
} */

void main () {
  var i = 0;
  while (i < 5) {
    var j = 0;
    while(j < 5) {
      print('$i-hi - $j-hi');
      j++;
    }
    i++;
  } 
}


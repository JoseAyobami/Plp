/*void main() {
  var i = 0;
  while (i < 11) {
    var j = 0;
    while (j < 11) {
      print('$i*$j = ${i * j}');
      j++;
    }

    i++;
  }
} */

void main() {
  var i = 0;
  do {
    var j = 1;
    do {
      print('$i*$j=${i * j}');
      j++;
    } while (j < 11);
    i++;
  } while (i < 11);
}

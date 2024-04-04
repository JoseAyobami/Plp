// conditional statement 
void main () {
double accountBalance = 1000.0;
double withdrawalAmount = 200.0;
if (withdrawalAmount <= accountBalance) {
  print("Withdrawal Sucessful. Remaining:\$${accountBalance.toStringAsFixed(2)}");
} else {
  print("Insuficient funds.");
}

 
List <double> transactions = [100.0, -50.0, 200.0, -75.0];
double totalBalance = 0.0;

for (var transaction in transactions) {
  totalBalance += transaction;
}
 print("Total balance:\$${totalBalance.toStringAsFixed(2)}");


bool isDeliveryAvailable = true;
int distanceFromResturant = 5; // in kilometres
if (isDeliveryAvailable && distanceFromResturant <=10) {
  print("Delivery is available.Placing order....");

} else {
  print("Delivery is unavailable or distance too far....");
}

}


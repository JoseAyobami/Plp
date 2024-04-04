'''def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
     #prompting the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the original price of the item: "))    

# calculate final price and printin the result
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after applying the discount:", final_price) '''



def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price -(price * (discount_percent / 100))
        return discounted_price
    else:
        return price

# prompting the users to input
original_price = float(input("Enter the price of the item: "))
discount_percentage = float(input("Enter the price of the item: " ))
 # calculate the final and print
 
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after applying the discoun: ", final_price)
    
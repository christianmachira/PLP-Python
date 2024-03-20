# creating a program that calculates the discounted price of an item 
# creating a function that prompts the user to enter the price of an item and the discount percentage
# if the discount is larger than 20%, print out the price, else print out the original price

def calculate_discount():
    # prompt user to enter price and discount
    price = float(input("Enter the price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    discount = price -(price * (discount_percentage / 100))
    
    # iterative function to check whether item is viable for discount
    if discount_percentage >= 20:
        print("The discounted price is: ", discount)
    else:
        print("The original price is: ", price)

calculate_discount()



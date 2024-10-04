# Shopping Cart
item_purchased=input("What do You want to buy ? : ")
price_of_item=float(input("what is the price of the item ? : "))
quantity=int(input("How many of the items do you want ? :  "))
total_price=price_of_item*quantity
print("Thanks for shopping with VMART SHOPPING".center(60,"="))
print(f"Your Total for {quantity} items of {item_purchased} is : ${total_price}")
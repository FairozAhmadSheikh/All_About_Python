shop={
    "laptop":{"price":200,"quantity":2},
    "mobile":{"price":100,"quantity":0},
    "pendrive":{"price":50,"quantity":3},
    }

# Just for Decoration
print("**************************")
print("What we have in our shop ")
# Loop for displaying items
for items in shop:
    print(items)
print("**************************")

# Asking user what they want to buy
to_buy=input("enter what you want to buy")

# Check if we have that element in our shop
if to_buy in shop.keys():
    
    quantity=int(input("How many do you want ?"))   # Accepts quantity
    # Condition to check whether we have sufficent stock 
    if quantity<shop[to_buy]["quantity"]:
        # If we have Stock we will process the amount
        print(f"Your Total Price will be : {quantity*shop[to_buy]["price"]}")
        print("Order Confirmed ")
    # If we dont have this much stock we can display this message
    else:
        print(f"We only have {shop[to_buy]["quantity"]} stock left , Try ordering in this range")
# if user inputs something that is not in our shop        
else:
    print("We dont have that in our stock")

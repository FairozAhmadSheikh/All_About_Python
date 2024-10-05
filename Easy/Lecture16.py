# Shopping Cart Program 
items=[]  
prices=[]
total_price=0

while True:
    item=input("What Do you want to Buy: (Q to quit)")
    if item.lower()=="q":
        break
    else:
        price=float(input(f"What is the price of {item} $"))
        items.append(item)
        prices.append(price)
print()
print("------BILL HERE------")
for item in items:
    print(item,end=" ")
for price in prices:
    total_price+=price
print()
print(f"Your Total is : $ {total_price}")
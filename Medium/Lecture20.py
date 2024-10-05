# Concession Stand Program 
menu={
    "pizza":3.99,
    "hamburger":6.99,
    "shawarma":9.97,
    "popcorn":4.55,
    "chips":5.55
}
cart=[]
total_price=0

print("------ MENU ------")
for key,value in menu.items():
    print(f"{key:10} : {value:.2f}$")

while True:
    item=input("What do you want to order ?  (Q to Quit) : ").lower()
    if item=="q":
        break
    elif menu.get(item):
        cart.append(item)
        # total_price+=menu.get(item) # Works but i will replace it by something else 
        
for food in cart:
    total_price+=menu.get(food)
    print(food,end=" ")
print()
print("------- BILL HERE -------")
print(f"Your Total is : ${total_price:.2f}")
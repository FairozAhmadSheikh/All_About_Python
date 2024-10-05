"""While Keeps on running untill some condition is true 
   below example of while loop will keep looping untill you enter Some name 
   """

name=input("Enter Your Name : ")
while name=="":
    print("You Didn't Enter Your Name : ")
    name=input("Enter Your Name : ")
print(f"Hello {name}")

food=input("Enter The Food You Like (Q to quit) : ").upper()

while not food=="Q":
    print(f"You Like {food}")
    food=input("Enter Another Food You Like (Q to quit) : ").upper()
print("Bye ")
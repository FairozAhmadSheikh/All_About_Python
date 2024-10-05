#For loop is used to itterate for some particular times 

for i in range(1,11):
    print(i)
    
# Continue is used to skip current itteration eg 13 in our below case
    
for x in range(1,21):
    if x==13:
        continue
    else:
        print(x)

# Break is used to break outof loop completely if that condition is met
for x in range(1,21):
    if x==13:
        break
    else:
        print(x)
           
# Nested Loops
"""Nested Loop is  A loop inside loop """

for x in range(4):
    for y in range(1,11):
        print(y,end="") # Prints without line break for inner loop
    print() # Line break after main loop's single iterartion completes
    

# Rectangle Printing using above logic

rows=int(input("Enter Number of Rows : \n"))
columns=int(input("Enter Number of Columns : \n"))
symbol=input("Enter a Symbol or Special Character : \n")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()
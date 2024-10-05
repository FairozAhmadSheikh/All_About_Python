
fruits=["apple","mango","orange"]
vegetables=["Turnip","Cabbiage","Raddish"]
meats=["chicken","lamb","Beef"]

"""2D Lists means a list inside list same like a Matrix 
   2D Collection in genneral means collection inside collection
    """

grocerries=[fruits,vegetables,meats]
# print(grocerries[0][0])
# print(grocerries[0][1])
# print(grocerries[0][2])
# print(grocerries[1][0])
# print(grocerries[1][1])
# print(grocerries[1][2])
# print(grocerries[2][0])
# print(grocerries[2][1])
# print(grocerries[2][2])


# Prints Whole 2D List
print(grocerries)

# Printing using nested loops 
for list in grocerries:
    for food in list:
        print(food)
    print()
    
# 2D Tuples

num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()
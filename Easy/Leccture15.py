"""Collections  are single variables to store multiple data values
1 list   [] ordered and changable    Duplicates allowed 
2 tuples () ordered and unchangable  Duplocates allowed  , Fastre
3 sets   {} unorderd & immutable     Duplicates Not allowed ,ADD REMOVE allowed
4 dictionaries {"key":"value"}  Key Value pairs where keys cannot be duplicates
"""
fruits=["Mango","Apple","Kiwi","Pineapple"]
print(fruits)
print(fruits[1:3])
print(fruits[::2])
print(fruits[::-1])# Reverses the list

for fruit in fruits:
    print(fruit)
    
# How to see help releated to methods in strings
print(dir(fruits))
# print(help(fruits))  # Helps in finding methods

# Methods of a collection 
print(len(fruits)) # returns length of friuts


# Checcking a particular item in Collections 

result="apple" in fruit
print(result)


# List Methods

#Append  item
fruits.append("Promegranate")
print(fruits)

# Remove item
fruits.remove("Kiwi")
print(fruits)

# insert item 
fruits.insert(0,"Dragon Fruit")
print(fruits)

# Sort Array 
fruits.sort()
print(fruits)

# Reverse a list 
fruits.reverse()
print(fruits)

# Clear a list

# fruits.clear()
# print(fruits)

# Finding the index of particular item
print(fruits.index("Apple"))

# No of occourences of element in a list 
fruits.append("Apple")
print(fruits.count("Apple"))


# Sets are unordered and immutable duplicates are ignored
# We cannot do indexing in sets as they are un-ordered
# We cannot change elements in a set but we can add remove elemnets
set1={"cat","dog","horse","hamster","elephant"}

# Mehods (length , in ,remove ,clear) common
print(len(set1))            # Length
print("cat" in set1)        # Finding element
set1.remove("elephant")     # Remove Particular
set1.pop()                  # removes one element at random
# set1.clear()              # Clears a set

# Add method is used to add elemnet in a set
set1.add("hiipo")
print(set1)

 # Tuples are orderded and unchangable 
 # Tuples allow duplicates 
 # Faster than Lists
 
tuple1=("crow","mango",35.7,"mango")

# Methods of tuples => len, in , index , count
print(tuple1.index("crow"))
print(len(tuple1))
print(tuple1.count("mango"))
print(35.7 in tuple1)


# Lecture 16 will be exercise on The List , Tuples and Sets 

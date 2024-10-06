# Itterables = an object or collection that can return its elements one at a time allowing it to be itterated over a loop
numbers=[1,2,3,4,5]
name="Feroz Ahmad"
s1={"apple","mango","crow","cat"}
dictionary={"A":1,"B":2,"C":3}
# For strings
for char in reversed(name):
    print(char,end=" ")
print()

# For Set  # Set cant be reversed 
for val in s1:
    print(val)

# Dictionary
for key ,values in dictionary.items():
    print(f"{key}:{values}")

# Itteration
for number in numbers:
    print(number)
    
# Reverse itteration

for number in reversed(numbers):
    print(number)
    
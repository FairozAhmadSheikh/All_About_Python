# List Comprehension 
"""A concise way to create lists in python
   Compact and easier to read than traditional loops
   [expression for value in itterable if condition]"""
   
# Traditional Approach 
doubles=[]
for x in range(1,11):
    doubles.append(x*2)
print(doubles)

# List Comprehension  Approach
double_list=[x*2 for x in range(1,11) ]
print(double_list)
double_list=[x*2 for x in range(1,11) if x%2==0 ]
print(double_list)
double_list=[x*2 for x in range(1,11) if x%2==1 ]
print(double_list)
# List of strings
fruits=["apple","mango","pears","coconuts"]
fruits=[fruit.upper() for fruit in fruits ]
print(fruits)

grades=[85,86,91,60,46,31]

passed_grades=[grade for grade in grades if grade>=60]
print(passed_grades)
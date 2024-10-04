import math
# Circumfrance of a circle 2 * 3.14 (pie) *r 
radius=float(input("Enter Radius of Circle : "))
# Logic
circumference=2 * math.pi * radius
# Output
print(f"Circumfrance of circle is : {round(circumference,2)} cm")

# Area of Circle = pie*r^2

# Logic 1
area_of_circle=math.pi * radius ** 2

# Or Logic 2 
area_of_circle=math.pi* pow(radius,2)

#Output
print(f"Area of Circle is : {round(area_of_circle,3)} cm^2")


# Hypotenus of A Triangle 

side1=float(input("Enter Side one of the rectangle ? : "))
side2=float(input("Enter Side two of the rectangle ? : "))

# Logic 
hypotnuese=math.sqrt((side1**2)+(side2**2))
print(f"Hypotenues is equal to : {round(hypotnuese,2)}")
# Module 
"""Module is a  file containing code that you want to include in your program use import to include module (Built-in  or your own ) ,module is usefull to divide the large program into reuseable seperate files """
#Ways of importing 
import math
import math as m
from math import pi

# Using imported modules
print(math.pi)
print(m.pi)
print(pi)

# Importing self created  module named (example)
import Example

print(Example.pi)
print(Example.cube(3))
print(Example.square(3))

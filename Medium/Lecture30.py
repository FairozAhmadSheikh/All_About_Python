# Variable Scope : is where variable is both visible and accessible
# Scope Resolution :(LEGB)=> Local,Enclosed,Global,Built-in

def func():
    a=10 # A is local to func and can be accesed only in func, func is like a house and can see evething inide but not the inside of other fxn
    print(a)
    print(c)
    
def func2():
    b=20 # B is local to func2 and can be accesed only in func2
    print(b)
    print(c)
    
c=56 # Global variable and can be accessed by everyone 

func()
func2()

# bulit in
from math import e

def new():
    print(e)
    
# e=3.65       # This will be value of e because of Rule Local > Enclosed> Global > Built-in
new()
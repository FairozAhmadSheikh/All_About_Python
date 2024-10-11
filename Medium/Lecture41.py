# Polymorphism  is derived from a greek word which means to have many faces or forms  poly=> many and morhe => faces 
"""   Two ways to achieve polymorphism
   1 : Inheritance= An object could be treated of the same type as a parent class
   2 : Duck Typing= Object must have necessary attributes and methods, object must have the minimum necessary attributes / methods 
    If it looks like a duck and quacks like a duck , it must be a duck"""
    
class Animal:
    is_alive=True
    
class Dog(Animal):
    def speak(self):
        print("Woof! ")
        
class Cat(Animal):
    def speak(self):
        print("Meowwwwwww!")
    

class Car:   # Car has minimum attributes and methods and can be considered as same class animal as it has both speak and is_alive 
    is_alive=False
    def speak(self):
        print("Honk! ")

instances=[Cat(),Car(),Dog()]

for instance in instances:
    instance.speak()
    print("Is Alive "if instance.is_alive else "Not Alive ")
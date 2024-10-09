# Inheritance = allows  a class to inherit attributes and methods from another class helps with code reuseability and extensibility.

class Animal:
    
    def __init__(self,name):
        self.name=name;
        self.is_alive=True;
    def eat(self):
        print(f"{self.name} is Eating ")
    def sleep(self):
        print(f"{self.name} is Sleeping ")

class Dog(Animal):
    def speak(self):
        print("WOOF!")
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Mouse(Animal):
    def speak(self):
        print("SQUEAK!")

dog=Dog("Scooby")
cat=Cat("Tom")
mouse=Mouse("Jerry")

print(dog.name)
dog.speak()
print(cat.name)
cat.speak()
print(mouse.name)
mouse.speak()
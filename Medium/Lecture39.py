# Multiple inheritance means a class is inherting from more than one parent
# Multi-level inheritance => inherits from a parent which inherits from another parent


class Animal:
    
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is Eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is Hunting")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is Fleeing")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


fish=Fish("Golden Fish")
rabbit=Rabbit("Bugs Bunny")
hawk=Hawk("Eagle")

fish.flee()
fish.hunt()

rabbit.flee()

hawk.hunt()

fish.eat()
fish.sleep()
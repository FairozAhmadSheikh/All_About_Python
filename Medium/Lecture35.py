# Object=A "bundle" of related attributes (variables) and methods(function)
# class = blueprint used to design the structure and layout of an object

class Car:
    def __init__(self,model,year,color):
        self.model=model;
        self.year=year;
        self.color=color;
    
    def start(self):
        return f"{self.color} {self.model}  Has Started "
    def stop(self):
        print(f"{self.color} {self.model} has Stopped ")
        
    def describe_car(self):
        return f"{self.color} {self.model} {self.year}"
    

car1=Car("Mustang",2016,"green")

print(car1.start())
print(car1.describe_car())
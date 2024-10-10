# Super => function used in child class to call methods from a parent class(super class).
#  Allows you to extend the functionality of inherited methods 
# Note : Useful for method overloading.


# In below examples i have wrote area formulas that not be actually correct so adjust accordingly

class Shapes:
    def __init__(self,color,is_filled):
        self.color=color;
        self.is_filled=is_filled;
    def describe(self):
        print(f"{self.color} and  {'Is Filled ' if self.is_filled else "Not filled"}" )


class Circle(Shapes):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius;
        #Method overloading means overloading a super method and also can be used to extend functionality show below
    def describe(self):
        super().describe()
        print(f"Area of Cirele is {3.14*self.radius**2} cm^2")
        

class Triangle(Shapes):
    def __init__(self,color,is_filled,height,width):
        super().__init__(color,is_filled)
        self.height=height;
        self.width=width;
  #Method overloading means overloading a super method and also can be used to extend functionality show below
    def describe(self):
        super().describe()
        print(f"Area of Triangle is {self.height*self.width/2} cm^2")
        
class Square(Shapes):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width;
        #Method overloading means overloading a super method and also can be used to extend functionality show below
    def describe(self):
        super().describe()
        print(f"Area of Square is {self.width**2} cm^2")
        
        
square=Square("Red",True,32)
square.describe()

circle=Circle("Green",False,22)
circle.describe()

triangle=Triangle("Orange",True,64,32)
triangle.describe()
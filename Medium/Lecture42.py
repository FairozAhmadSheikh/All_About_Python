# Static Method : Is a method that belongs to a class rather than any object created from that class ,generally static methods are used as utility functions

"""
1 : Instance Methods : Best for Operations on Instances of the class (objects)
2 : Static Methods : Best for utility functions that dont need access to class data
"""

class Employee:
    def __init__(self,name,position):
        self.name=name;
        self.position=position;
    # Instance Method as it will depend on the object or instance created below
    def get_info(self):
        return f"{self.name}={self.position}"
    # Static method it is method of a class and can be called without object creation
    @staticmethod
    def is_valid_position(position):
        valid_positions=["CEO","Manager","Doctor"]
        return position in valid_positions
    


# Static Method
print(Employee.is_valid_position("Manager"))

# Instance Method
employee1=Employee("Amir","CEO")      
print(employee1.get_info())  

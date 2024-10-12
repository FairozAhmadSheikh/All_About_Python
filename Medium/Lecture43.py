# Class Methods allow operation related to class itself, they take (cls) as first parameter
"""
1: Instance Methods : Best for operations on instances of classes(objects)
2: Static Methods : Best for Utility functions where access to class data is not needed
3: Class Methods : Best for class level data or require access to class itself
"""

class Student:
    count=0
    total_gpa=0
    
    def __init__(self,name,gpa):
        self.name=name;
        self.gpa=gpa;
        Student.count+=1;
        Student.total_gpa+=gpa
    
    @classmethod
    def total_students(cls):
        return f"Total Number of Students is : {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average GPA Is :{cls.total_gpa/cls.count:.2f} "
        
std1=Student("Ali",3.2)
std2=Student("Mohd",4.4)
print(Student.average_gpa())
print(Student.total_students())


    

        
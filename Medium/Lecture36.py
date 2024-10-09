# Class Variable is shared among all instances of the class , and is defined outside the constructor 
# allows you to share data among all objects created from that data

class Students:
    # class variables
    num_students=0;
    class_year=2024;
    
    # Constructor 
    def __init__(self,name,age):
        #Attributes
        self.name=name;
        self.age=age
        Students.num_students+=1
    

student1=Students("Fairoz",26)
student2=Students("Sameer",28)

# Attributes printing
print(student1.name,student1.age)
print(student2.name,student2.age)
# print(student1.class_year)  # Not the best way to class variables 

# Class Varible printing best way

print(Students.class_year)
print(f"Total Number of students : {Students.num_students} are Graduating in year {Students.class_year}")



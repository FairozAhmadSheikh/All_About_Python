# Mmebership Operators are used to check whether a value is in sequence or not (String, list ,dict,set or tup)  types are ,  1: in   2 : not in

# Example 
secret_word="MAHINDRA"
guess=input("Enter A Guess character : ").upper()

# Use case for in 
if guess in secret_word:
    print("You got it Correct ")
else:
    print('Incorrect ! Try again')
    
# Use case for not in 
if guess not in secret_word:
    print("You Got it wrong ")
else:
    print("You got it correct")
    
# List tuple and set use case for in is same 

list1=["Crow","Elephant","Dog","Sparrow"]
finder=input("Enter something to find in List : ").capitalize()
if finder in list1:
    print(f"{finder} is in list ")
else:
    print(f"{finder} is not in list")
    
# Dictionary in and not in
result_cards={"Sponge":"A",
              "Ali":"A+",
              "Umar":"D"
              }
student=input("Enter A Name of Student : ")
if student in result_cards:
    print(f"{student}'s grade is :{result_cards.get(student)}")
else:
    print(f"{student}'s Result not available ! ")
    
# Email Validator
email=input("Enter Email to receive your result ")

if "@" in email and "." in email:
    print("Valid Email , Email sent ")
else:
    print("Not a Valid Email ")
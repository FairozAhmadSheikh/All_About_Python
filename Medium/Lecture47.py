# Exception Handling => Exception Is an event that that interupts normal flow of the program 
#  Value Error , ZeroDivisonError, Type Error

try: 
    number=int(input("Enter A NUMBER  : "))
    print(1/number)
except ZeroDivisionError:
    print("Cant divide by Zero ")
except ValueError:   # if user types something except a number
    print("Enter Numbers only please ")

finally:
    # Usefull in File Handling
    # This Part Executes no matter what 
    print("Finally i am cleaning up something ")
# Match Case Statements (Switch Case Statements ):
""" an alternative to using elif statements ,Executes some code if a value matchs a case Benifits : Cleaner and Syntax is more readable """
# Traditioanl If else and elif 
def day_of_week(day):
    if day==1:
        print("Its Sunday")
    elif day==2:
        print("Its Monday")
    elif day==3:
        print("Its Tuesday")
    elif day==4:
        print("Its Wednsday")
    elif day==5:
        print("Its Thursday")
    elif day==6:
        print("Its Friday")
    elif day==7:
        print("Its Saturday")
    else:
        print("Not a valid day")
        
day_of_week(4)

# Match case
def day_of_week(day):
    match day:
        case 1:
            print("Its Sunday")
        case 2:
            print("Its Monday")
        case 3:
            print("Its Tuesday")
        case 4:
            print("Its Wednsday")
        case 5:
            print("Its Thursday")
        case 6:
            print("Its Friday")
        case 7:
            print("Its Saturday")
        case _:
            print("Not a valid day")

day_of_week(1)
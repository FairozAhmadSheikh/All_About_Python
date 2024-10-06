# Functions A block of reusable code 
# Position of parameters matter always 
# Paramters are just temperory data sent to function
# Arguments are data sent to function
"""Return is a statement used to end a function and send a result back to caller"""
# Positional Arguments
def happy_birthday(name,years):
    print(f"Happy Birthday to you!{name}")
    print(f"You! Are {years} Old")
    print("Happy Birthday to you!")
    print()

happy_birthday("Feroz",33)
happy_birthday("Sameer",35)
happy_birthday("Hussain",31)

# Default Arguments are default value for a certain parameters Default is used when the argument is ommitted , default arguments make function more flexible and reduce number of parameters

def net_price(list_price,discount=0,gst=0.18):
    calc=list_price*(1-discount)*(1+gst)
    return calc
print(net_price(100))

import time  # Should be at Top

def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    return("Done !")
print(count(0,10))


# Keyword Argumnets 
"""An argument preceded by an identifier helps with readablility , order of arguments doesnot matter here"""

def phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

# Positional Argumnets order matters
phone_num=phone(91,788,952,1098)
print(phone_num)
# Keyword aguments order does not matter
phone_num2=phone(country=91,first=952,last=1098,area=788)
print(phone_num2)

# Arbitary arguments means varying amount of argumets 
"""We have two main types of arbitary arguments
1: *args: allows to pass  non key argumnets
2" **kwargs: allows to pass  keyword  arguments
   *: Refers to unpacking operator
"""
# Example for args
def add(*args):
    total=0
    for arg in args:
        total+=arg
    return total

print(add(1,2,3,4,5))


# Example for **kwargs

def print_addr(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    
    
print_addr(street="121 Botakadal",
           city="Srinagar",
           landmark="Masjid"
           )    


# Both args and kwargs example

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")

shipping_label("Dr","Ali","Abbas","Askari",
               street="141 Pakistan",
               city="Lahore",
               landmark="Imam Bargah",
               zipcode=190074
               )
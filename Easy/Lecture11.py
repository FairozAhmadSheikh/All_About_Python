# Validating User input
""" Username is not more than 12 charcters 
    Username Must not contain spaces
    Username must not contain digits """

username=input("Enter Username : ")
length=len(username)
if length>12:
    print("Your Username cant be more than 12 characters ")
elif username.find(" ")>0:
    print("Your Username cant conatin spaces")
# elif username.isdigit()==False:
#     print("Username Cannot contain Numbers")
elif not username.isalpha():
    print("Username cant contain Numbers")
else:
    print(f"Welcome {username}")
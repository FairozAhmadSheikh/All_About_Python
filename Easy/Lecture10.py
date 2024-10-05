# String Methods
name="Fairoz Ahmad"
# Len is used to find length 
print(len(name))

# Find used to find first occourance of element
result=name.find(" ") # Finds Space and gives index 
print(result)

# rFind used to find last occourance of element
result=name.rfind("a") # Finds Space and gives index 
print(result)

# capitalize upper lower 
print(name.upper())
print(name.lower())
print(name.capitalize())

# is digit tells if a string conatins only digits 
print(name.isdigit())
value="1230"
print(value.isdigit())

# is alpha tells if a string conatins only alphabets 
# Only returns true if there are no numbers and spaces
namee="ISam"
print(namee.isalpha())

# Replace Methods 
phone_number="+91-7889-52-10-98"
phone_number=phone_number.replace("-","")
print(phone_number)

# String Indexing  [start:end:step]
credit_card_number="4524-5987-6604-3280"
print(credit_card_number[::2]) # Starts from 0 ends when completes step takes +2
print(credit_card_number[2:6]) # Starts from 2 index ends at 6 where 6 is exlusive and 2 is inclusive
print(credit_card_number[-1])# Last index or from reverse side 

#Last digits online card like 

last_digits=credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")





# Excercise for this topic in Next lecture 

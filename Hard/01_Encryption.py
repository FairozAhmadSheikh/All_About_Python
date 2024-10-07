import random
import string


# We will encrypt some messages of user and Decrypt them back

# What we need 
# 1 All Alphabets ,digits and punctutaion and balnk space for encrytion 
chars=string.ascii_letters+string.digits+string.punctuation+" "

# for seperation  of individual charcters make a list of chars
chars=list(chars)  

# Everytime the chars should shuffle so i created a new copy of  list and  shuffled it

key=chars.copy()
random.shuffle(key)



# User Input For Encryption

plain_text=input("Enter A Message To Encrypt : ")
cipher_text=""

# Itterate Through every letter of the plain_text find its index in chars and then append it to encrypted it in a way that place the word of key [index ] in it 

# Encryption
for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]
print(f"Plain Text Entered : {plain_text}")
print(f"Encrypted Text : {cipher_text}")


# User Input for Decryption
cipher_text=input("Enter Cipher Text To decrypt :")
plain_text=""
# Decryption
for letter in cipher_text:
    index=key.index(letter) 
    plain_text+=chars[index]
    
print(f"Decrypted text is :{plain_text}")


# Dictionaries Are key value pairs dictionaries can be nested also ,
# Dictionaries are orderd  and changeable  with no dupliactes  allowed 

capitals={
    "usa":"washington",
    "india":"new delhi",
    "germany":"berlin",
    "iran":"tehran",
    "pakistan":"lahore",
}
print(capitals)

# Get Method to get value of any key
print(capitals.get("iran"))

# Update method to update a value in dictionary  or adds new if key doesnot exist

capitals.update({
    "singapore":"malaysia"
})
print(capitals)


# Remove key value pair
capitals.pop("india")
print(capitals)

# popitem will remove the latest element that is inserted 
capitals.popitem()
print(capitals)

# clear clears whole dictionary
# capitals.clear()

# keys method and value methods

print(capitals.keys())
print(capitals.values())


# Loop through keys and value
for key in capitals.keys():
    print(key)
for value in capitals.values():
        print(value)

# Items returns key values in the form of tuples

for item in capitals.items():
    print(item)
    
    
# Key value using loop

for key,value in capitals.items():
    print(f"{key}:{value}")
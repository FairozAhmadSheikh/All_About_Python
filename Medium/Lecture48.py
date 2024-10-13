import os 
# File Detection : Detecting files 

# Absolute Path
file_path="C:\\Users\\habra\\Desktop\\python"
# Relative is something in same folders or in nested same  folder 
# file_path="test.txt"   # if its in same folder
if os.path.exists(file_path):
    print(f"yes    '{file_path}    Exists'")
    if os.path.isdir(file_path):
        print("Its a Directory ")
    elif os.path.isfile(file_path):
        print("It is a file ")
else:
    print("Location does not exist")
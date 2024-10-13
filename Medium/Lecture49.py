# File Handling => Read and Write operations on files (.txt,.json,.csv)



"""Txt Data """
text_data="I love Python \n"

file_path="Handling_text.txt"

try:
    with open(file_path,"w") as file:   # x = create new , w= Overwrite data , a=append data
        file.write(text_data)
        print("Sucessfully done ")
except FileExistsError:
    print("File Already Exists Try appending or over writing the file")


""""Json Data   (key value form data) """

student={
    "name":"Ali",
    "age":26,
    "job":"Job Less"
    
}

import json

file_path="HandlingJSON.json"

try:
    with open (file_path,"w") as file:
        json.dump(student,file,indent=4)
        print("Sucessfully wrote json file")
except FileExistsError:
    print("File Already Exists Try appending or over writing the file")
    

# Handling CSV Files like  excel sheets and 2d lists (Comma Seperated Data)

import csv

employees=[
    ["Name","age","Job"],
    ["Patrick",20,"CEO"],
    ["Sameer",21,"HOD"],
    ["Hussain",25,"SHO"],
    ]

file_path="HandlingCSV.csv"
try: 
    with open (file_path,"w") as file:
        writer=csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print("Successfully wrote a csv file ")
except FileExistsError:
    print("File Already Exists Try appending or over writing the file")
    
    
# Adding a list to some file 

group_students=["eesa","Hussain","Sameer","Feroz"]
file_path="Handling_text.txt"

try :
    with open (file_path,"a")as file:
        for value in group_students:
            file.write(value+"\n")
        print("Sucessfully done ")
except FileExistsError:
    print("File Already Exists Try appending or over writing the file")
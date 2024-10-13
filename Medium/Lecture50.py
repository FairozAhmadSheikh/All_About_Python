# Reading Data 
import csv
import json




# Txt files
file_path="Handling_text.txt"

try:
    with open(file_path,'r')as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("File Not Found Maybe You Deleted it")
    
# JSON file

file_path="HandlingJSON.json"

try :
    with open(file_path ,"r")as file:
        content=json.load(file)
        print(content)
except FileNotFoundError:
    print("File Not Found Maybe You Deleted it")
    
# CSV File

file_path="HandlingCSV.csv"
try:
    with open (file_path,'r') as file:
        content=csv.reader(file)
        for lines in content:
            print(lines)
except FileNotFoundError:
    print("File Not Found Maybe You Deleted it")
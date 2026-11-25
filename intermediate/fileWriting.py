# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "C:\\Users\\Phoenix\\Desktop\\output.txt"

# w - write a file
# x - write if it doesn't already exist.
# a - append, any new data will be appended to that file

with open(file_path, "w") as file: # 'with' will open and close the file when we're done with it
    # 'open' will return a file obj, the first parameter is the file path the second is the mode "w" means write  
    file.write(txt_data)
    #print(f"txt file {file_path} was created")
    #print(f"data wrote: {txt_data}")

# Collections

employees = ["Eugene", "Siri", "Robert"]
with open(file_path, "w") as file: 
  
    for employee in employees:
        file.write(employee+"\n")
    # print(f"txt file {file_path} was created")
    # print(f"data wrote: {employees}")

# Json file

import json

employee = {
    "name": "Steve",
    "age": 30,
    "job": "cook"
}

with open(file_path, "w") as file: 
  
    json.dump(employee, file, indent=4) # dump -> dictionary to a json string
    print(f"txt file {file_path} was created")
    print(f"data wrote: {employees}")


# CSV COMMA SEPARATED VALUES
import csv

employees3 = [["Name", "Age", "Job"],
            ["Luiz", 18, "dev"], 
            ["New", 8, "kid"],
            ["Old", 78, "grandpa"]]


with open(file_path, "w", newline="") as file: 
  
    writer = csv.writer(file)
    for row in employees3:
        writer.writerow(row)
    print(f"txt file {file_path} was created")
    print(f"data wrote: {employees}")


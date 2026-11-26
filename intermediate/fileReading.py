
import json
import csv
# Writing 
file_path = "C:\\Users\\Phoenix\\Desktop\\output.json"
data = {
    "name": "luiz",
    "age": 18
}
with open(file_path, "w") as file:
    json.dump(data, file)


# reading a json file
try:

    with open(file_path, "r") as file: # r read
        content = json.load(file)
        print(content['name'])



except FileNotFoundError:
    print("File not Found.")
except PermissionError:
    print("You do not have permission to read that file.")
except Exception:
    print("Something went wrong.")

# CSV FILE

with open(file_path, "r") as file: # r read
    content = csv.reader(file)
    for line in content:
        # print(line[0]) # access a column name for example
        pass


  


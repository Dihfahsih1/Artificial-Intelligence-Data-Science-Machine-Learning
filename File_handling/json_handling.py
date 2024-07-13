import json 
# reading from the json file
def read_json_file(file_param):
    with open(file_param,'r') as file:
        data=json.load(file)
        return data
    
#writing json data to a file
def write_json_file(data,file_to):
    with open(file_to, 'w') as file:
        json.dump(data, file, indent=2)

  
filename="files/users.json" #location of the file to be processed  
json_read_data=read_json_file(filename) # function call assigned to a variable json_read_data


new_person={
    "id":00000,
    'name':"John",
    "city":"Kampala",
    "age": 10,
}
json_read_data.append(new_person)

write_json_file(json_read_data,filename)
print(json_read_data)
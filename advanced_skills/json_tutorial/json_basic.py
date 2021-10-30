import json

# encoding dict to json

person = {
    "name" : "yi",
    "age" : 30,
    "city" : "Hsinchu",
    "marriage" : False
}

person_json = json.dumps(
    person, 
    indent=4, # looks nicer in console and save files
    sort_keys=True # sort keys alphabetically if true
    )
print("dict: ", person)
print("json: ", person_json)

with open("person.json", "w") as file:
    json.dump(
        person, 
        file,
        indent=4
        )

# decoding json, from json --> dict

# load and loads are different, loads is from memory
person_dict = json.loads(person_json) 
print(person_dict)

# load is from files
with open("person.json", "r") as file:
    person_loaded = json.load(file)
    print(person_loaded)
# serialize

# deserialize

import json
with open("person.json") as file:
    data = json.load(file)

# json-string


print(data)
print(type(data))
print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])


import json

with open("users2_key.json") as file:
    users=json.load(file)

print(users)
print("-------------------------------")
print(users["mehmetKonyali"])
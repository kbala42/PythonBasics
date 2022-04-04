import json

with open("users2_key.json") as file:
    users=json.load(file)

print(users)
print("-------------------------------")

users.pop("huseyinKonyali")

with open("users2_key.json","w") as fie:
    json.dump(users,fie,ensure_ascii=False,indent=2)
import json

with open("users2_key.json") as file:
    users=json.load(file)

print(users)
print("-------------------------------")

users.update({
    "hasanKonyali":
    {
        "firstName": "Hasan",
        "lastName": "Konyali",
        "age":25
    }
})

with open("users2_key.json","w") as fie:
    json.dump(users,fie,ensure_ascii=False,indent=2)
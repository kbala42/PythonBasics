import json
userEkle={
    "userName": "mehmetKonyali",
    "firstName": "Mehmet",
    "lastName": "Konyali"
}

with open("users.json") as file:
    users=json.load(file)

print(type(users))

for user in users:
    print(user)
print("--------------------------------------------------------------")
print(user)
print("--------------------------------------------------------------")
users.append(userEkle)
for user in users:
    print(user)

with open("users.json","w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
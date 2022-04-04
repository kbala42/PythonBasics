import json

with open("users.json") as file:
    users=json.load(file)
for user in users:
    print(user)
print("----------------------------------")
for user in users:
    if user["userName"]=="hasanKonyali":
        user["userName"]="hasan_konyali"

for user in users:
    print(user)

with open("users.json","w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
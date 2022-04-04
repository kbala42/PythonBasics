import json

with open("users.json") as file:
    users=json.load(file)
for user in users:
    print(user)
print("----------------------------------")
users.remove(users[0])

for user in users:
    print(user)

with open("users.json","w") as file:
    json.dump(users, file, ensure_ascii=False, indent=2)
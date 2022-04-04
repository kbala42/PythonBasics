import json
with open("db.json") as file:
    db=json.load(file)

print(db)
print("----------------------------------")
print(db["users"])
print("----------------------------------")
print(db["products"])
print("----------------------------------")
print(db["users"]["mehmetKonyali"])
print("----------------------------------")
print(db["users"]["mehmetKonyali"]["firstName"])
print("----------------------------------")
print(db["products"]["1"])
print("----------------------------------")
print(db["products"]["1"]["productName"])
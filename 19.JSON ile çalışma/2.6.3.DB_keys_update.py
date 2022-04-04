import json
with open("db.json") as file:
    db=json.load(file)

db["products"].update({
    "3":{
        "productName": "IPhone 7",
        "price": 7000
    }
})
db["users"].update({
    "hakanKonyali":{
        "firstName": "Hakan",
        "lastName": "Konyali"
    }
})

with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)

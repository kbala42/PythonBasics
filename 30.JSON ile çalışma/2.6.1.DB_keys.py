db={
    "users":{
        "huseyinKonyali": {
            "firstName": "Huseyin",
            "lastName": "Konyali"
        },
        "mehmetKonyali": {
            "firstName": "Mehmet",
            "lastName": "Konyali"
        }
    },
    "products":{
        "1":{
            "productName":"IPhone 8",
            "price":5000
        },
        "2": {
            "productName": "IPhone 12",
            "price": 8000
        }
    }
}
import json
with open("db.json","w") as file:
    json.dump(db,file,ensure_ascii=False,indent=2)
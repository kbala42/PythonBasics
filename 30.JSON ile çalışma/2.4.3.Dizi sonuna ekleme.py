data=[
    {
        "userName":"hasanKonyali",
        "firstName":"Hasan",
        "lastName":"Konyali"
    },
    {
        "userName": "huseyinKonyali",
        "firstName": "Huseyin",
        "lastName": "Konyali"
    }
]
import json
with open("users.json","a") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
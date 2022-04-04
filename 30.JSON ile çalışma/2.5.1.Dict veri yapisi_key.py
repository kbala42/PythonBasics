
data={
    "huseyinKonyali":{
        "firstName": "Huseyin",
        "lastName": "Konyali"
    },
    "mehmetKonyali":{
        "firstName": "Mehmet",
        "lastName": "Konyali"
    }
}
import json

with open("users2_key.json","w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
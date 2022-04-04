data={
    "userName":"hasanKonyali",
    "firstName":"Hasan",
    "lastName":"Konyali"
}
import json
with open("users.json","w") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
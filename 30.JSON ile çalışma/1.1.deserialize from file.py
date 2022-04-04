import json # gelen json verilerini yapılandırmak için
with open("person.json") as file:
    #data = file.read()#direkt okumak için
    data = json.load(file)# Gelen bilgiler artık dict formatındadır
print(data)
print(type(data))
print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])
print(data["children"])
print(data["children"][0])
print(data["children"][0]["age"])

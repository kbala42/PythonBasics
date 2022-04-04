import json # gelen json verilerini yapılandırmak için
person ="""
{
    "firstName":"Sadık",
    "lastName":"Turan",
    "hobbies":["spor","sinema"],
    "age":37,
    "children":[
        {
            "firstName":"Çınar",
            "age":4         
        },
        {
            "firstName":"Ahmet",
            "age":2         
        }

    ]
}
"""
print(person)
print(type(person))

sonuc=json.dumps(person,ensure_ascii=False,indent=2) #serialize işlemi çıkış str
# ensure_ascii=False Türkçe karakterler için
# indent=2 yapı

print(sonuc)
print(type(sonuc))

with open("person.json","w") as file:
    json.dump(person, file, ensure_ascii=False, indent=2)


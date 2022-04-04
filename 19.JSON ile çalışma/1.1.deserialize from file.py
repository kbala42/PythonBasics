'''
---------------------------------------------------------tw:@tek_elo
Python'da JSON formatında gelen verileri yapılandırmak için
json modülünü kullanıyoruz
--------------------------------------------------------------------
'''
# gelen json verilerini yapılandırmak için modülü içeriyoruz
import json
# file adıyla person.json dosyasını açıyoruz
with open("person.json") as file:
    #data = file.read()#direkt okumak için

    # Gelen bilgileri dict formatına dönüştürüyoruz ve data'da saklıyoruz
    data = json.load(file)

# data tipini öğreniyoruz
print(type(data))
# data içeriğini yazdıryoruz
print(data)

print(data["firstName"])
print(data["hobbies"])
print(data["hobbies"][0])
print(data["children"])
print(data["children"][0])
print(data["children"][0]["age"])

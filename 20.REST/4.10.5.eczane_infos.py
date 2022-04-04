import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

api="apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
headers = {
    'content-type': "application/json",
    'authorization': api
    }

#il=input("ili giriniz: ")
#ilce=input("İlçe giriniz: ")
il="Konya"
ilce="Karatay"
sorgu= "/health/dutyPharmacy?ilce="+ilce+"&il="+il

conn.request("GET",sorgu , headers=headers)

print("------------örnek res http.client.HTTPResponse sınıfından bir nesne ------------------")
res = conn.getresponse()
print(type(res))
print(res)
print("------------------------------\n")

print("\n----------örnek data 'bytes' tipinde dönüş alıyoruz--------------------\n")
data = res.read()
print(type(data))
print(data)
print("------------------------------\n")
dict=json.loads(data.decode("utf-8"))
print(type(dict))
print(dict)
print(dict["result"])
for d in dict["result"]:
    print(d["address"])



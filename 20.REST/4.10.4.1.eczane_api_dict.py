import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
    }

#il=input("ili giriniz: ")
#ilce=input("İlçe giriniz: ")
il="Konya"
ilce="Karatay"
sorgu= "/health/dutyPharmacy?ilce="+ilce+"&il="+il

conn.request("GET",sorgu , headers=headers)

res = conn.getresponse()

data = res.read()

dict=json.loads(data.decode("utf-8"))
print(type(dict))
print(dict)
print(dict["result"])
for d in dict["result"]:
    print(d["address"])



import http.client
import json
conn = http.client.HTTPSConnection("api.collectapi.com")

api="apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
headers = {
    'content-type': "application/json",
    'authorization': api
    }

il=input("ili giriniz: ")
ilce=input("İlçe giriniz: ")

sorgu= "/health/dutyPharmacy?ilce="+ilce+"&il="+il

conn.request("GET",sorgu , headers=headers)

res = conn.getresponse()

data = res.read()

dict=json.loads(data.decode("utf-8"))

for d in dict["result"]:
    print('Ad: ', d['name'])
    print('Bölge: ', d['dist'])
    print('Adres: ',d['address'])
    print('Telefon: ', d['phone'])
    print('Konum: ', d['loc'])



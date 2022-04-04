import requests
import json

api_key="apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"
api_adres= "https://api.collectapi.com/health/dutyPharmacy?"
headers = {
    'content-type': "application/json",
    'authorization': api_key
}

il="Konya"
ilce="Karatay"

sorgu= api_adres+"il="+il+"&ilce="+ilce

data= requests.get(sorgu,headers=headers)
print(type(data))
print(data)
print("-----------------------------------------")

dict=data.json()

if dict["success"]==True:
    for d in dict["result"]:
        print('Ad: ', d['name'])
        print('Bölge: ', d['dist'])
        print('Adres: ',d['address'])
        print('Telefon: ', d['phone'])
        print('Konum: ', d['loc'])
        print("https://maps.google.com/maps?q=" + d["loc"] + "&hl=es&z=14")
else:
    print("Nöbetçi eczane listesi alınamadı...")



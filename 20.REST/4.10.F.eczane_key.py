import requests
import json

base_url="https://api.collectapi.com/health/dutyPharmacy?"
baslik={
    "content-type" : "application/json",
    "authorization": "apikey 1wW9AlMoINturjcKue6q1y:1ZmA7Vx0tzMlJB7mqVr2nT"
}

il=input("İl Giriniz")
ilce=input("İlçe Giriniz")

#data= requests.get(sorgu,headers=headers)

r=requests.get(base_url+"il="+il+"&ilce="+ilce,headers=baslik).json()
for a in r["result"]:
    print (a["name"])

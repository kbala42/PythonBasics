import requests
import json

adres="https://api.collectapi.com/health/dutyPharmacy"
token="1wW9AlMoINturjcKue6q1y:1ZmA7Vx0tzMlJB7mqVr2nT"

baslik = {
'content-type': "application/json",
'authorization': "apikey " + token
}

print("---------------------------")
eczane_ili=input("ECZANE İL : ")
eczane_ilcesi=input("ECZANE İLÇE : ")
print("---------------------------")
sorgu=f"{adres}?il={eczane_ili}&ilce={eczane_ilcesi}"
print(sorgu)
veri= requests.get(
    sorgu,
    headers=baslik
).json()

if veri["success"]==True:
    liste = veri["result"]
    for eczanesi in liste:
        print(eczanesi["name"])
        print("ADRES : ",eczanesi["address"])
        print("ILETISIM : ",eczanesi["phone"])
        print("---------------------------")
else:
    print("Nöbetçi eczane bilgisi alınamadı..")
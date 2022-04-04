import requests
import json

class NobetciEczaneBul():
    def __init__(self, il, ilce=""):
        self.__il = il
        self.__ilce = ilce
        self.__apiAddress = f"https://api.collectapi.com/health/dutyPharmacy?il={il}&ilce={ilce}"
        self.__apiKey = "apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"

    def __bul(self):
        header = {'content-type': "application/json",'authorization': self.__apiKey}
        data=requests.get(self.__apiAddress,headers=header)
        dict=data.json()
        return dict['result']

    @property
    def yazdirNobetciEczane(self):
        nobetListesi = self.__bul()
        for nobetci in nobetListesi:
            print("---------------------------------------------")
            print(f"Ad: {nobetci['name']}")
            print(f"Bölge: {nobetci['dist']}")
            print(f"Telefon:{nobetci['phone']}")
            print(f"Adres: {nobetci['address']}")
            print(f"Konum: {nobetci['loc']} ")
            print(f"https://maps.google.com/maps?q={nobetci['loc']}&hl=es&z=14")

il=input("İli giriniz:")
ilce=input("İlçeyi giriniz:")
nobetci=NobetciEczaneBul(il,ilce)
nobetci.yazdirNobetciEczane





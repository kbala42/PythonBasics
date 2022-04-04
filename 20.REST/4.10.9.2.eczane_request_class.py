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

        if dict['success'] == True:
            return dict['result']
        else:
            return [{'name':"bulunamadı",'address':"bulunamadı"}]

    @property
    def bulNobetciEczane(self):
        nobetListesi = self.__bul()
        for nobetci in nobetListesi:
            print(
            f"""
            **************************************************************************
            Ad: {nobetci['name']}
            Bölge: {nobetci['dist']}
            Telefon:{nobetci['phone']} 
            Adres: {nobetci['address']}
            Konum: {nobetci['loc']}            
            **************************************************************************
            """
            )

il=input("İli giriniz:")
ilce=input("İlçeyi giriniz:")
nobetciEczane=NobetciEczaneBul(il,ilce)
nobetciEczane.bulNobetciEczane



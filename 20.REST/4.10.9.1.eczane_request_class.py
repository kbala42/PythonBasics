import requests
import json

class NobetciEczaneBul():
    def __init__(self, il, ilce=""):
        self.__il = il
        self.__ilce = ilce
        self.__apiAddress = f"https://api.collectapi.com/health/dutyPharmacy?il={il}&ilce={ilce}"
        self.__apiKey = "apikey 7y6402nf3JlgOOXjpHrC6l:0ntMNqbmC6oDidBA5xCLEs"

    @property
    def getIl(self):
        return self.__il

    @property
    def getIlce(self):
        return self.__ilce

    @property
    def setIl(self, il):
        self.__il= il

    @property
    def setIlce(self, ilce):
        self.__ilce = ilce

    def __getir(self):
        header = {'content-type': "application/json",'authorization': self.__apiKey}
        data=requests.get(self.__apiAddress,headers=header)
        dict=data.json()

        if dict['success'] == True:
            return dict['result']
        else:
            return [{'name':"bulunamadı",'address':"bulunamadı"}]


    @property
    def getNobetciler(self):
        liste = self.__getir()
        for eczane in liste:
            print(
            f"""
            **************************************************************************
            Ad: {eczane['name']}
            İlçe: {eczane['dist']}
            Telefon:{eczane['phone']} 
            Adres: {eczane['address']}
            Konum: {eczane['loc']}            
            **************************************************************************
            """
            )

il=input("İli giriniz:")
ilce=input("İlçeyi giriniz:")
nobetciEczane=NobetciEczaneBul(il,ilce)
nobetciEczane.getNobetciler



import requests
import json

class NobetciEczaneler():
    def __init__(self, apiKey, il, ilce=""):
        self.__il = il
        self.__ilce =ilce
        self.__base_url = f"https://api.collectapi.com/health/dutyPharmacy?ilce={ilce}&il={il}"
        self.__apiKey = apiKey

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
        token = self.__apiKey
        baslik = {'content-type': "application/json",'authorization': token}
        r=requests.get(self.__base_url,headers=baslik).json()
        if r['success'] == True:
            return r['result']
        else:
            return [{'name':"bulunamadı",'address':"bulunamadı"}]


    @property
    def getNobetciler(self):
        liste = self.__getir()
        for eczane in liste:
            print(
            f"""
            **************************************************************************
            Adı = {eczane['name']}
            Adresi = {eczane['address']}
            İlçesi = {eczane['dist']}
            **************************************************************************
            """
            )

ili = input("İl giriniz")
ilcesi = input("ilcenizi giriniz.")
apikey = input("ApiKeyinizi giriniz.")
nbt=NobetciEczaneler(apikey,ili,ilcesi)
nbt.getNobetciler

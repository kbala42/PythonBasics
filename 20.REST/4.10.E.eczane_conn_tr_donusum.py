import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
'content-type': "application/json",
'authorization': "apikey 70qCa5iEtrqzeW2VIMVV96:6rKZb1NTY9dGCXqkIJQnEJ"
}

BilgiGirisiYanlis=0

def eczaneler(_Dict):
    for eczane in _Dict:
        print("Nöbetçi Eczane Adı :", eczane["name"])
        print("Nöbetçi Eczane Adresi :", eczane["address"])
        print("Nöbetçi Eczane Telefonu :", eczane["phone"])
        print("*****************************************************************")
def eczane(eczane):
    print("Nöbetçi Eczane Adı :", eczane["name"])
    print("Nöbetçi Eczane Adresi :", eczane["address"])
    print("Nöbetçi Eczane Telefonu :", eczane["phone"])

def trHarfCevir(gelenMetin):
    sayac=0
    htmlTurkceHarfDict = {"ı": "%C4%B1", "ç": "%C3%A7",
    "ş": "%C5%9F", "ö": "%C3%B6",
    "ü": "%C3%BC", "ğ": "%C4%9F",
    "İ": "%C4%B0", "Ç": "%C3%87",
    "Ş": "%C5%9E", "Ö": "%C3%96",
    "Ü": "%C3%9C", "Ğ": "%C4%9E"}
    cevirilenMetin=""
    for n in gelenMetin:
        for harf in htmlTurkceHarfDict.keys():
            if harf == n:
                if sayac == 0:
                    cevirilenMetin= gelenMetin.replace(harf, htmlTurkceHarfDict[harf])
                else:
                    cevirilenMetin = cevirilenMetin.replace(harf, htmlTurkceHarfDict[harf])
                    sayac = +1
            if sayac == 0:
                return gelenMetin
            else:
                return cevirilenMetin

"""


girilenIl =input("İl Giriniz? ")
if girilenIl!="":
    il=str(trHarfCevir(girilenIl))
    BilgiGirisiYanlis = 0
else:
    BilgiGirisiYanlis=1
    girilenIlce =input("İlçe Giriniz? ")
if girilenIlce!="":
    ilce=str(trHarfCevir(girilenIlce))
    BilgiGirisiYanlis = 0
else:
    BilgiGirisiYanlis = 1

if BilgiGirisiYanlis==0:
    link ="/health/dutyPharmacy?ilce="+ilce+"&il="+il
    conn.request("GET", link, headers=headers)
    res = conn.getresponse()
    data = res.read()
    veri=data.decode("utf-8")
if not("false" in veri):
veri=veri.replace("{\"success\":true,\"result\":[","")
veri=veri.replace("]}","")
Dict = eval(veri)
dicLength=len(Dict)
if dicLength==5:
eczane(Dict)
else:
eczaneler(Dict)
else:
print("Girdiğiniz bilgiler yanlış!!!")
else:
print("Bilgileri boş giremezsiniz!!!")

"""
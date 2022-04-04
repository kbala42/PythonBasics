"""
Rezervasyon yapan ve rezervasyon kaydını kontrol eden program
"""
def RezervasyonYap():
    rezervasyonBilgisi=input("rezervasyon bilgilerinizi giriniz")
    veri=rezervasyonBilgisi+","
    dosya=open("rezervasyon.txt","a")
    dosya.write(veri)
    dosya.close()

def RezerevasyonKontrol() :
    rezervasyonbilgisi=input("rezervasyon bilgilerinizi giriniz")
    with open("rezervasyon.txt","r") as dosya:
        veri=dosya.read()
        rezervasyonlar=veri.split(",")
        if rezervasyonbilgisi in rezervasyonlar:
            print("rezervasyonunuz bulunmaktadır.")
        else:
            print("rezervasyon kaydınız yoktur.")

while True:
    islem=input("rezervasyon yapmak için 1 : kontrol için 2 programı kapatmak için  3 e basınız")
    if islem=="1" :
        RezervasyonYap()
    elif islem =="2":
        RezerevasyonKontrol()
    else:
        break
import random
import time

"""
Kodlama Egzersizimizde yazdığımız Kumanda Sınıfına ek olarak metodlar ve özellikler eklemeye çalışın.
"""
class Kumanda():

    def __init__(self, tvDurum = "Kapalı", tvSes = 0, kanalListesi = ["TRT"], kanal = ["TRT"]):
        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi=kanalListesi
        self.kanal=kanal

    def tv_ac(self):

        if (self.tvDurum == "Açık"):
            print("Televizyon zaten açık....")
        else:
            print("Televizyon Açılıyor...")
            self.tvDurum ="Açık"

    def tv_kapat(self):

        if(self.tvDurum == "Kapalı"):
            print("Televiyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tvDurum ="Kapalı"

    def ses_ayarla(self):

        while True:
            cevap = input("Sesi azalt: '<'\nSesi arttır: '>'\nÇıkış: çıkış")

            if (cevap == "<"):
                if (self.tvSes != 0):
                    self.tvSes -= 1
                    print("Ses:",self.tvSes)

            elif (cevap == ">"):
                if (self.tvSes != 51):
                    self.tvSes += 1
                    print("Ses:",self.tvSes)

            else:
                print("Ses Güncellendi:",self.tvSes)
                break

    def kanal_ekle(self, kanalIsmi):

        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanalListesi.append(kanalIsmi)
        print("Kanal eklendi.")

    def rastgele_kanal_sec(self):

        rastgele = random.randint(0,len(self.kanalListesi)-1)

        self.kanal = self.kanalListesi(rastgele)

        print("Şu an ki kanal:",self.kanal)

    def __len__(self):

        return len(self.kanalListesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi {}\nŞu anki kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)

kumanda = Kumanda()

print("""
    Televizyon Kumandası
    
    1. Tv Aç
    2. Tv Kapat
    3. Ses Ayarları
    4. Kanal Ekle
    5. Kanal Sayısını Öğrenme
    6. Rastgele Kanala Geçme
    7. Tv Bilgileri
    
    Çıkmak için 'q' ya basın.


""")

while True:

    islem = input("İşlemi seçiniz:")

    if(islem == "q"):
        print("Program sonladırılıyor...")

    elif (islem == "1"):
        kumanda.tv_ac()

    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem == "3"):
        kumanda.ses_ayarla()

    elif (islem == "4"):
        kanalIsimleri = input("Kanal isimlerini ',' ile ayırarak giriniz.")

        kanalListesi = kanalIsimleri.split(",")

        for eklenenler in kanalListesi:
            kumanda.kanal_ekle(eklenenler)

    elif (islem == "5"):

        print("Kanal Sayısı:".len(kumanda))

    elif (islem == "6"):
        kumanda.rastgele_kanal_sec()

    elif (islem == "7"):
        print(kumanda)

    else:
        print("Geçersiz işlem...")
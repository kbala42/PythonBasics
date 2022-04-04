class Personel():
    def __init__(self,isim,maas,departman):
        print("Personel sınıfının init fonksiyonu")

        self.isim=isim
        self.maas=maas
        self.departman = departman
    def bilgileriGoster(self):
        print("Personel sınıfının bilgileri.")

        print("isim: {}\nMaaş: {}\nDepartman: {}\n".format(self.isim,self.maas,self.departman))

    def departmanDegistir(self, yeniDepartman):
        self.departman = yeniDepartman

class Yonetici(Personel):
    def zamYap(self, zamMiktari):
        self.maas += zamMiktari

yonetici=Yonetici("Ahmet",5000,"Perseonel Amiri")

yonetici.bilgileriGoster()

yonetici.departmanDegistir("İnsan Kaynakları")

yonetici.bilgileriGoster()

print(dir(yonetici))

yonetici.zamYap(1000)

yonetici.bilgileriGoster()
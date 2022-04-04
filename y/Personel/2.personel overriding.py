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
    def __init__(self,isim,maas,departman,kisiSayisi):
        print("Yönetici sınıfının init fonksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisiSayisi=kisiSayisi

    def bilgileriGoster(self):
        print("Yönetici sınıfının bilgileri.")

        print("isim: {}\nMaaş: {}\nDepartman: {}\nSorumlu Kişi Sayısı: {}".format(self.isim, self.maas, self.departman,self.kisiSayisi))

    def zamYap(self, zamMiktari):
        self.maas += zamMiktari

yonetici=Yonetici("Ahmet",5000,"Perseonel Amiri",5)

yonetici.bilgileriGoster()




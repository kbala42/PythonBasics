class Kedi():
    tur='Memeli'

    def __init__(self, adi, yasi):
        self.adi=adi
        self.yasi=yasi

    def Ozellikler(self):
        return "{} {} yaşında".format(self.adi,self.yasi)

    def Miyavla(self, sesi):
        return "{} {} diye miyavlar".format(self.adi,sesi)


# Kedi alt sınıfından miras alan alt sınıf
class PersKedisi(Kedi):
    def Tuyleri(self, tuyuNasil):
        return "{} tüyleri {}".format(self.adi, tuyuNasil)

class VanKedisi(Kedi):
    def GozRengi(self, gozRengiNe):
        return "{} gözleri {}".format(self.adi, gozRengiNe)

    def Ozellikler(self):
        return "Türü: Van kedisi adı:{} ve {} yaşında".format(self.adi, self.yasi)

#overridding
pisi = VanKedisi('Pisi', 4)
print(pisi.Ozellikler())
print(pisi.GozRengi('Mavi ve kahverengi'))
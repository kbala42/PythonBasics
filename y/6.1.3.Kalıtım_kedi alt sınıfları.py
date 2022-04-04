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

# Alt sınıftan “Pisi” adında ve “4” yaşında bir kedi türetiniz.
pisi=VanKedisi('Pisi',4)
print(pisi.Ozellikler())
print(pisi.GozRengi('Mavi ve Kahverengi'))
print("------------------------")
persia= PersKedisi('Persia', 4)
print(persia.Ozellikler())
print(persia.Miyavla('meaaaw'))
print(persia.Tuyleri('Yumuşak'))
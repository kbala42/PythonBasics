class MasaLambasi:
    __doc__ = 'Masa Lambası Sınıfı'
    isikDurumu=False

    def __init__(self, isikSiddeti,isikRengi='Sarı',garantiSuresi=2):
        self.isikSiddeti=isikSiddeti

    def IsikAc(self):
        self.isikDurumu=True

    def IsıkKapat(self):
        self.isikDurumu=False

    def IsigiArttir(self, arttirmaMiktari):
        self.isikSiddeti += arttirmaMiktari

masaLambasi=MasaLambasi(60,garantiSuresi=3)
print("Işık açık mı? :", masaLambasi.isikDurumu)
masaLambasi.IsikAc()
print("Işık açık mı? :", masaLambasi.isikDurumu)
print("Işık şiddeti:",masaLambasi.isikSiddeti,"lx")
masaLambasi.IsigiArttir(10)
print("Işık şiddeti:",masaLambasi.isikSiddeti,"lx")
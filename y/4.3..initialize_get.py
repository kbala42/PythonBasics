class Kare:
    def __init__(self,kenar):
        self.kenar = kenar
    def getKenar(self):
        return self.kenar
    def alanHesapla(self):
        self.alan=self.kenar*self.kenar
        return self.alan

kare=Kare(5)
print("Kenar: ",kare.getKenar())
kare.kenar=8
print("Kenar: ",kare.getKenar())



class Kedi():
    tur='Memeli'

    def __init__(self, adi, yasi):
        self.adi=adi
        self.yasi=yasi

    def Ozellikler(self):
        return "{} {} yaşında".format(self.adi,self.yasi)

    def Miyavlama(self, sesi):
        return "{} {} diye miyavlar".format(self.adi,sesi)
class Ogrenciler():
    def __init__(self, sorgu=None,sirasi=None):
        self.ogranciListe=[('Murat Çalışkan',11,131),('Ahmet Birinci',11,124),('Emre Hızlı',12,135),('Murat Çalışkan',12,155)]
        if not sorgu and not sirasi:
            listem=self.ogranciListe
        else:
            listem=[li for li in self.ogranciListe if sorgu == li[sirasi]]
        for i in listem:
            print(*i,sep=', ')

    @classmethod  # Bir sınıf metodu tanımlanıyor
    def OgrenciAdindanSorgula(cls, adi):  # self gibi burada da cls parametresi kullanılıyor
        cls(adi, 0)

    @classmethod
    def OgrenciSinifindanSorgula(cls, sinifi):
        cls(sinifi, 1)

    @classmethod
    def OgrenciNumarasindanSorgula(cls, numarasi):
        cls(numarasi, 2)

# Doğrudan sınıfın metotlarını çağırarak ve adını verdiğiniz bir öğrencinin bilgilerini listeleyiniz.
Ogrenciler.OgrenciAdindanSorgula('Murat Çalışkan')

#  Belirli bir sınıftaki öğrencilerin listesini alınız.
Ogrenciler.OgrenciSinifindanSorgula(12)

# Öğrenci numarasından sorgulama yapınız.
Ogrenciler.OgrenciNumarasindanSorgula(131)
print("----------------------------------------")

#Tüm öğrencileri listelemek için Ogrenciler() argüman kullanmadan çağırmalısınız. Bunun için sınıfınızdan
#bir nesne türetiniz.
tumOgrenciListe=Ogrenciler()
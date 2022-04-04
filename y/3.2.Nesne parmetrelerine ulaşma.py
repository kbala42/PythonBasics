'''
---------------------------------------------------------tw:@tek_elo
Verilen metin ifadelerini istenilen kadar yazan bir sınıf tanımlayınız.
__init__ fonksiyonu başlangıçta her zaman yürütülen fonksşyondur
--------------------------------------------------------------------
'''
# MetinSinifi
class MetinSinifi:
    # init fonksiyonunu tanımlıyoruz
    def __init__(self, ifade, tekrarSayisi=5, kacisKarakteri="\n"):
        self.ifade=ifade
        self.tekrarSayisi=tekrarSayisi
        self.kacisKararkteri=kacisKarakteri
        print((ifade + kacisKarakteri) * tekrarSayisi)
metin=MetinSinifi("Merhaba")
print("Tekralanan metin:",metin.ifade)
print("Tekrar sayısı:",metin.tekrarSayisi)
print("Kaçış karakteri:",metin.kacisKararkteri)

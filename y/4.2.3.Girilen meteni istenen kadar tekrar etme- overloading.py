"""
Verilen metin ifadelerini istenilen kadar yazan bir sınıf tanımlayınız.
Sınıf için bazı zorunlu parametreler oluşturulacaktır.
"""
class MetinSinifi:
    def __init__(self, ifade, tekrarSayisi=5, kacisKarakteri="\n"):
        #print(ifade * tekrarSayisi,kacisKarakteri)
        print((ifade + kacisKarakteri) * tekrarSayisi)
metin=MetinSinifi("Merhaba")

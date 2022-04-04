class Kitap():
    def __init__(self, isim, yazar, sayfaSayisi, tur):
        print("Kitap nesnesi oluşturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayisi = sayfaSayisi
        self.tur = tur
    def __str__(self):
        return "İsim:{}\nYazar:{}\nSayfa Sayısı:{}\nTür:{}".format(self.isim,self.yazar,self.sayfaSayisi,self.tur)
    def __len__(self):
        return self.sayfaSayisi
    def __del__(self):
        print("Kitap nesnesi siliniyor...")

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit", 561,"Polisiye")

print(kitap) # __str__ metodu

#print(len(kitap)) # __len__ metodu

#del kitap # __del__ metodu

print(kitap)
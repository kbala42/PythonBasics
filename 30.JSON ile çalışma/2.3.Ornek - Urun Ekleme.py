def urunEkle(urunAdi, fiyat, satistaMi, kategoriler):
    urun={
        "urunAdi":urunAdi,
        "fiyat":fiyat,
        "satistaMi":satistaMi,
        "kategoriler":kategoriler
    }

    import json
    with open("urunler.json","w") as file:
        json.dump(urun,file,ensure_ascii=False)

# urunEkle("iphone 12", 8000,True,["telefon","elektronik"])

def urunGetir():
    import json
    with open("urunler.json") as file:
        urun=json.load(file)

    kategoriler=' '.join([kategori for kategori in urun["kategoriler"]])
    print(kategoriler)
    print(f'Ürün Adı:{urun["urunAdi"]} Fiyatı:{urun["fiyat"]} Kategoriler:{kategoriler}')

urunGetir()
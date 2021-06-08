"""
Bir çiftçi sizden tüm hayvanlarının bacak sayısını söylemeniz konusunda yardım istiyor. Çiftçide üç tür hayvan var:
tavuk, inek, koyun *Sırasıyla
Çiftçi hayvanlarını saydı ve size tüm türlerin alt toplamını verdi. Tüm hayvanların toplam bacak sayısını döndüren bir
fonksiyonu uygulamanız gerekiyor.
"""
def hayvanlar(tavuk, inek, koyun):
    toplam_ayak_sayisi = tavuk * 2 + inek * 4 + koyun * 4
    return toplam_ayak_sayisi

print(hayvanlar(3, 4, 2))
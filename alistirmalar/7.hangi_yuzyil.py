"""
Hangi Yüzyıl?
    Tarihi alan ve doğru yüzyıla döndüren bir fonksiyon oluşturun.
Örnekler
yuzyil(1756) -»"18. yüzyıl”
yuzyil(1555) -> ”16. yüzyıl”
"""
def yuzyil(yil):
    n=yil//100
    if yil%100>0:
        n+=1
        return "{s}. yüzyıl".format(s=n)


print(yuzyil(1532))
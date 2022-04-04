dosya=open("veri2.csv","r")
"""
for satir in dosya:
    print(satir)
"""
"""
for satir in dosya:
    liste=satir.split('","')
    print(liste)
"""

artis_sayisi=0
azalis_sayisi=0

for satir in dosya:
    liste=satir.split('","')
    print(liste)
    if "-" in liste[5]:
        print(liste[0]," tarihinde", liste[5],"oranında düşüş yaşandı")
        azalis_sayisi+=1
    else:
        print(liste[0]," tarihinde", liste[5],"oranında artış yaşandı")
        artis_sayisi+=1

print(" dolar kuru ", azalis_sayisi, " oranında düşüş yaşandı")
print(" dolar kuru ", artis_sayisi," oranında artış yaşandı")

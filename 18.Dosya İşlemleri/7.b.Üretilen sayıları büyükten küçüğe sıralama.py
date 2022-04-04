"""
Üretilen sayıları büyükten küçüğe sıralama
"""
dosya=open("sayi.txt","r")
sayilar=dosya.readlines()
dosya.close()
# sayıları string olarak aldık sayıya dönüştürüp sıralayıp tekrardan stringe dönüştüreceğiz
for i in range(len(sayilar)):
    sayilar[i]=int (sayilar[i])

sayilar.sort()

for i in range(len(sayilar)):
    sayilar[i]=str(sayilar[i])+"\n"

dosya=open("sırali.txt","w")
dosya.writelines(sayilar)
dosya.close()
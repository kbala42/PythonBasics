asalSayi=[2]
for sayi in range (3,1001):
    for bolenSayi in range (2,sayi):
        sayiAsalmi=False
        if sayi % bolenSayi==0:
            sayiAsalmi=True
            break
    if sayiAsalmi==False:
        asalSayi.append(sayi)
veri=" "
for i in asalSayi:
    veri+=str(i) # veri=veri+str(i)
    veri+=" "
dosya=open ("AsalSayi.txt","w")
dosya.write(veri)
dosya.close()
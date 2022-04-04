with open("AsalSayi.txt","r") as dosya :
    veri=dosya.read()
    asalSayilar=veri.split(" ")
kontrolSayisi=input("asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz")
if kontrolSayisi in asalSayilar :
    print("asal sayı")
else:
    print("asal sayı değil")
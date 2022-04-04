def notHesapla(satir):
    satir=satir[:-1]# okunan satır aralarındaki satır boşluklarını kaldırmak için
    print(satir)



with open("notlar.txt", "r",encoding="utf-8") as file:
    for i in file:
        notHesapla(i)
def notHesapla(satir):
    satir=satir[:-1]# okunan satır aralarındaki satır boşluklarını kaldırmak için
    liste=satir.split(",")
    isim=liste[0]
    not1 = liste[1]
    not2 = liste[2]
    final = liste[3]
    print("{} 1. vize notu:{}, 2. vize notu:{}, final notu:{}".format(isim,not1,not2,final))



with open("notlar.txt", "r",encoding="utf-8") as file:
    for i in file:
        notHesapla(i)
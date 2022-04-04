def notHesapla(satir):
    satir=satir[:-1]# okunan satır aralarındaki satır boşluklarını kaldırmak için
    liste=satir.split(",")
    isim=liste[0]
    not1 = int(liste[1]) # str to int
    not2 = int(liste[2])
    final = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + final * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"



with open("notlar.txt", "r",encoding="utf-8") as file:
    istenenListe=[]
    for i in file:
        istenenListe.append(notHesapla(i))
    print(istenenListe)
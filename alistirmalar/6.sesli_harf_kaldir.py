def sesli_kaldir(cumle):
    yeni_cumle=""
    sesli="aeıioöuüAEIİOÖUÜ"
    for i in cumle:
        if i not in sesli:
            yeni_cumle +=i
    return yeni_cumle

print(sesli_kaldir("Python problemi çözüyorum..."))
"""

Girilen metnin bütünüyle büyük veya küçük harflerden oluşuyorsa True döndüren fonksiyon yazın

"""
def ayni_mi(yazi):
    """
    if yazi.isupper():
        return True
    elif yazi.islower():
        return True
    else:
        return False
    """
    return yazi.isupper() or yazi.islower()

print(ayni_mi("python"))


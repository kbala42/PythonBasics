""""
"Kareler" isminde bir tane sınıf tanımlayın ve bu sınıfı iterable bir sınıf yapmaya çalışın. Bu sınıfın init fonksiyonu maksimum isimli bir tane parametre alsın ve her next işleminde ekrana üzerinde bulunduğunuz sayının karesi yazdırılsın. StopIteration hatası ekrana
maksimum sayıyı geçtiğiniz zaman fırlatılsın.
"""
class Kareler():

    def __init__(self,maksimum):
        self.maksimum = maksimum

        self.sayı = 1

    def __iter__(self):
        return self
    def __next__(self):

        if (self.sayı <= self.maksimum):

            sonuc =  self.sayı ** 2
            self.sayı += 1
            return sonuc
        else:
            self.sayı = 1
            raise StopIteration
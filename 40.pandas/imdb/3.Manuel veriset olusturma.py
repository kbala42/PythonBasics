print('----------------------------------------------------------tw:@tek_elo')
print('andom kütüphanesi kullanarak örnek bir array oluşturma-\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
import random
print('----r--------------------')
randomlist1 = random.sample(range(15, 25), 2)
randomlist2  = random.sample(range(15, 25), 2)
print(randomlist1)
print(randomlist2)

randomlistoflists = [randomlist1, randomlist2]
print(randomlistoflists)

print('----r--------------------')
columns = ["Sıcaklık 1.gün","Sıcaklık 2.gün"]
mydataframe = pd.DataFrame(randomlistoflists,index = ["İst","Ankara"],columns = columns)
print(mydataframe)
print(type(mydataframe))
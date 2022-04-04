print('----------------------------------------------------------tw:@tek_elo')
print('        imdb veritabanı\n')
print('******* kopya oluşturma *******\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
df = pd.read_csv('imdb_top_1000.csv')

print('--------df nesnesinin kopyasını alıp yazdırıyoruz--------------------')
df_kopya = df.copy()
print(df_kopya.head())
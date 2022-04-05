print('----------------------------------------------------------tw:@tek_elo')
print('        imdb veritabanı\n')
print('******* obje filtreleme *******\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
df = pd.read_csv('imdb_top_1000.csv')
print(df.head())

print('--------veri tabanı elaman tipleri---------------')
df_filtered = df[df['IMDB_Rating'] >= 8]
print(df.dtypes)

print('--------Runtime nesnesi içinde 1. elemanları alıp tablonun sonuna ekliyoruz---------------')
f = lambda x: (x["Runtime"].split())[0]
df["RuntimeYeni"] = df.apply(f, axis=1)
print(df['RuntimeYeni'])
print(df.head())
print(df.dtypes)

print('--------Üretilen sütun yine object, burada filtreleme yapmak için int dönüştürüyoruz--------------')
df['RuntimeYeni2'] = df['RuntimeYeni'].astype('int')
print(df.dtypes)
# şimdi yeni oluşan sütunda filtreleme yapabiliriz
df_filtered = df.query('RuntimeYeni2 >= 140')
print(df_filtered)

print('--------RuntimeYeni nesnesini siliyoruz---------------')
df = df.drop(['RuntimeYeni'], axis = 1)
print(df.head())

print('----------------------------------------------------------tw:@tek_elo')
print('        imdb veritabanı\n')
print('******* filtreleme *******\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
df = pd.read_csv('imdb_top_1000.csv')

print('--------IMDB_Rating 8 den büyükleri yazdırma---------------')
df_filtered = df[df['IMDB_Rating'] >= 8]
print(df_filtered)

print('--------IMDB_Rating 9.2 den büyükleri yazdırma---------------')
df_filtered2 = df[df['IMDB_Rating'] >= 9.2]
print(df_filtered2)

print('--------IMDB_Rating 9.2 den büyükleri query metodu ile yazdırma---------------')
df_filtered3 = df.query('IMDB_Rating >= 9.2')
print(df_filtered3)
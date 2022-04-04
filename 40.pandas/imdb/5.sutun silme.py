print('----------------------------------------------------------tw:@tek_elo')
print('        imdb veritabanı\n')
print('******* sütun ve satır silme *******\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
df = pd.read_csv('imdb_top_1000.csv')

print('--------\'Overview\'ve \'Meta_score\' sütunlarını silme---------------')
df_yeni = df.drop(['Overview', 'Meta_score'], axis = 1)
print(df_yeni.head())

print('--------Aynı işlem şu şekilde yapılabilir---------------')
df_yeni2 = df.drop(columns = ['Overview', 'Meta_score'])
print(df_yeni2.head())

print('--------satır silme---------------')
df_yeni3 = df.drop([1])
print(df_yeni3.head())
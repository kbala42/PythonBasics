print('----------------------------------------------------------tw:@tek_elo')
print('imdb veritabanı\n')
print('---------------------------------------------------------------------')
print()
import pandas as pd
df = pd.read_csv('imdb_top_1000.csv')
print('--------Esaretin Bedeli filminin ratingi----------------')
print(df['IMDB_Rating'][0])

print('--------Esaretin Bedeli filmine ait bilgiler-------------')
print(df.loc[df['Series_Title'] == 'The Shawshank Redemption'])

print('--------Baba filmine ait bilgiler-------------')
print(df.loc[df['Series_Title']=="The Godfather"])

print('--------Dönen bilgi Dataframe nesnesi-------------')
print(type(df.loc[df['Series_Title'] == 'The Shawshank Redemption']))

print('--------Esaretin Bedeli filmin yerini bilmiyorsak veri seti içinden bulabiliriz--------------')
print(df.loc[df['Series_Title'] == 'The Shawshank Redemption']['IMDB_Rating'])

print('--------IMDB_Rating değeri 8\'in üstünde olan ve No_of_Votes 100000den çok olan filmler-------------')
print(df.loc[(df['IMDB_Rating']>=8) & (df['No_of_Votes']>=100000)])

print('--------IMDB_Rating değeri 8\'in üstünde olan ve Gross değeri (yani gişe hasılatı) 30000000\'dan çok olanfilmler-------------')
#print(df.loc[(df['IMDB_Rating']>=8) & (df['Gross']>=30000000)])
print(df.dtypes)
# convert column "Gross" of a DataFrame
# to_numeric This function will try to change non-numeric
# objects (such as strings) into integers or floating point numbers as appropriate.
df['Gross'] = df['Gross'].str.replace(",", "")
df["Gross"] = pd.to_numeric(df["Gross"])
type(df["Gross"][0])
print(df.loc[(df['IMDB_Rating']>=8.0) & (df['Gross']>=500000000)])
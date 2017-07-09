import pandas as pd
import quandl

# api_key = 'm1o33y94x8Len_ivQ4W8'
# df = quandl.get("FMAC/HPI_AK", authtoken="m1o33y94x8Len_ivQ4W8", start_date="1999-01-31")
fs = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')


# df.set_index('Date', inplace=True)
# df.to_csv('ak_houseprice.csv')

# print(df.head)
# print(fs)
print(fs[0][0])

for abbv in fs[0][0][1:]:
    print("FMAC/HPI_"+ str(abbv))
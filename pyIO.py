import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
df = pd.read_csv('newcsv4.csv', names=['Date','Austin HPI'])

df.plot()
plt.show()

# df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')

# print(df.head())


# df.set_index('Date', inplace=True)
# df.to_csv('newcsv2.csv')

#
# df = pd.read_csv('newcsv2.csv',index_col=0)
# print(df.head())
#
# df.columns = ['Austin HPI']
# print(df.head())
#
# df.to_csv('newcsv3.csv')

# df = pd.read_csv('newcsv3.csv',index_col=0)
#
# df.to_csv('newcsv4.csv',header=False)

# df = pd.read_csv('newcsv4.csv', names=['Date','Austin HPI'])
# print(df.head())

# df.to_html('example.html')

# df.rename(columns={'Austin HPI': '77006_HPI '}, inplace=True)



# print(df.head())


# print(list_reallohn_week_vollzeit)
# print(list_reallohn_week_teilzeit)
# print(list_reallohn_week_mini)

# plt.plot([reallohn_2014_vollzeit,reallohn_2015_vollzeit,reallohn_2015_vollzeit_nb])
# plt.plot(list_reallohn_week_vollzeit, label = 'Vollzeit pro Woche')
# plt.plot(list_reallohn_week_teilzeit, label = 'Teilzeit pro Woche')
# plt.plot(list_reallohn_week_mini, label = 'Mini Job pro Woche')


# df_reallohn_week_vollzeit.set_index('Identifier')
# plt.bar(df_reallohn_week_vollzeit,height=3)
# plt.show()

# data = [['A', 1, 2], ['B', 2, 3], ['C', 3, 4]]
# df2 = pandas.DataFrame(data, columns=['Label', 'Col1', 'Col2'])
# df2.index = df2['Label']
# df2.plot(kind='barh')
# plt.show()
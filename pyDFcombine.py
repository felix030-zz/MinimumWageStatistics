import pandas as pd

# df3 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'Low_tier_HPI':[50, 52, 50, 53]},
#                    index = [2001, 2002, 2003, 2004])
# df2 = pd.DataFrame({'HPI':[80,85,88,85],
#                     'Int_rate':[2, 3, 2, 2],
#                     'US_GDP_Thousands':[50, 55, 65, 55]},
#                    index = [2005, 2006, 2007, 2008])

df1 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])



df3 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# use merge when the index does not matter to you
merged = pd.merge(df1,df3, on = 'Year', how='outer')
merged.set_index('Year', inplace= True)

# use join when the index matters to you
# use appending or concatination to enlong it 


print(merged)


# df1.set_index('HPI',inplace=True)
# df3.set_index('HPI',inplace=True)
# print(df1)
# print(df3)



# s = pd.Series([66, 26, 66], index = ['HPI','Int_rate','US_GDP_Thousands'])
# df4 = df1.append(s,ignore_index=True)
#
# concat = pd.concat([df1,df2,df3])
# print(concat)
# print(df4)

# print(pd.merge(df1,df2, on=['HPI','Int_rate']))
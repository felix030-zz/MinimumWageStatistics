import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day' : [1,2,3,4,5,6], 'Visitors' : [43,45,34,33,55,67], 'Bounce_Rate' : [62,64,65,77,44,23]}
df = pd.DataFrame(web_stats)


# select two columns
print(df[['Visitors','Bounce_Rate']])

#to list
print(df.Visitors.tolist())

# using numpy to combine two lists
print(np.array(df[['Visitors','Bounce_Rate']]))


# print(df)
# print(df.head())
# print(df.tail())
# print(df.tail(2))
# print(df.set_index('Day'))
# print(df.set_index('Visitors'))
#
# df2 = df.set_index('Day')
#
# print(df2.tail())
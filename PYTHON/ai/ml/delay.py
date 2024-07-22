import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



#df = pd.read_csv('delayPredict.csv')#load csv file
df = pd.read_csv('csv/delayPredict.csv')
df = df.replace(-9999, np.nan)
#df = df[['DAY_OF_WEEK']]

print('Rows in the data frame: {0}'.format(len(df)))#shows rows in the data frame
print('Rows without NAN: {0}'.format(len(df.dropna(how='any'))))#show not empty rows in the data frame
print(df.apply(lambda x: sum(x.isnull()), axis=0))# NAN allocation between columns
#del df['feature']#delete one column

#df['year'].plot(kind='hist')
#plt.plot(df['DAYS_OF_WEEK'])
#plt.hist(df['TAIL_NUM'],bins=30)#plot histogram
#plt.show()
print(df.head)

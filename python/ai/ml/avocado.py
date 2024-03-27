import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



df = pd.read_csv('csv/avocado.csv')
df = df.replace(-9999, np.nan)
#fill in NaN
#df.fillna(-9999, inpla=True)

print('Rows in the data frame: {0}'.format(len(df)))#shows rows in the data frame
print('Rows without NAN: {0}'.format(len(df.dropna(how='any'))), end='\n\n')#show not empty rows in the data frame
print(df.apply(lambda x: sum(x.isnull()), axis=0))# NAN(Not-A-Number - really is number) allocation between columns

#del df['feature']#delete one (not informative) column

#plot histogram
#df['year'].plot(kind='hist')
#plt.show()

#print(df.head)

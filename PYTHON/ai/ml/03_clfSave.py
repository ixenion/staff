import pandas as pd
#import quandl
import math, datetime
import numpy as np
from sklearn import preprocessing, svm#(svm - support vector machine)
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

#dataframe(df)
df = pd.read_csv('csv/wiki_googl.csv', header=0, index_col='Date', parse_dates=True)


df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
print(df.head)
#define new dataframe:
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)#data scaling. usexul when 1, 10, 400, 10000 and so on
x_lately = x[-forecast_out:]#here about 30 days
x = x[:-forecast_out]

df.dropna(inplace=True)#drop missing data
y = np.array(df['label'])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


#clf = LinearRegression(n_jobs=10)
#clf.fit(x_train, y_train)
##save##############################################
#with open('clfSave/linearRegres-3.pickle','wb') as f:
#    pickle.dump(clf, f)
####################################################

##use saved clf#####################################
pickle_in = open('clfSave/linearRegres-3.pickle','rb')
clf = pickle.load(pickle_in)
####################################################

accuracy = clf.score(x_test,y_test)


#prediction based on x data:

forecast_set = clf.predict(x_lately)
df['forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

#populate the dataframe with the new dates and forecast values

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

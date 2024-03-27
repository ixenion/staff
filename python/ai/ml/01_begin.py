import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm#(svm - support vector machine)
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#dataframe(df)
df = pd.read_csv('csv/wiki_googl.csv')

#load from web and save
#df = quandl.get('WIKI/GOOGL')
#df.to_csv('wiki_googl.csv')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

#define new dataframe:
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)#drop missing data

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])
x = preprocessing.scale(x)#data scaling. usexul when 1, 10, 400, 10000 and so on
y = np.array(df['label'])


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#old is:
#y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)
#with import cross_validation

#classifire (clf)
#clf = LinearRegression()#first algorithm.
#clf.fit(x_train, y_train)#fit clf and train it. to fit features and lables
#accuracy = clf.score(x_test,y_test)#calculate accuracy [1; -1]
#print(accuracy)

#clf = svm.SVR()#second algorithm. does lot worse then first one
#clf.fit(x_train, y_train)#to fit or train a clf. to fit features and lables
#accuray = clf.score(x_test,y_test)
#print(accuracy)

clf = LinearRegression(n_jobs=10)#training will be faster (n_jobs=-1 as many jobs as possible)
clf.fit(x_train, y_train)#to fit or train a clf. to fit features and lables
accuracy = clf.score(x_test,y_test)
print(accuracy)
#print('')
#print(df.head)
#df['Adj. Close'].plot(kind='hist')
#plt.show()

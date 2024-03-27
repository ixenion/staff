import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm#(svm - support vector machine)
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#import scikit-learn dataset library
from sklearn import datasets

#load dataframe
wine = datasets.load_wine()#not csv?
#dataframe storage
#('/usr/local/lib/python3.8/dist-packages/sklearn/datasets/data/wine_data.csv')

#print the names of the features
print(f"names of the features: \n{wine.feature_names}")

#print the label species(class_0, class_1, class_2)
print(f"names of the labels: \n{wine.target_names}")

#print top 5 data records
print(f"top 5: \n{wine.data[0:5]}")

#print wine labels (not names, but value)
print(f"wine labels value: \n{wine.target}")

#print data(feature) shape
print(f"data(feature) shape: \n{wine.data.shape}")

#print target(label) shape
print(f"target(label) shape: \n{wine.target.shape}")

#splitting data to tain - test
#import train_test_split function
from sklearn.model_selection import train_test_split

#split data into train test set
x_train, x_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)#70% train and 30% test

#generating model for k=5
from sklearn.neighbors import KNeighborsClassifier

#create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)

#train the model using the training set
knn.fit(x_train, y_train)

#predict the responce for test dataset
y_pred = knn.predict(x_test)

#accuracy estimation
from sklearn import metrics
#model accuracy, how often is the classifier correct?
print("Accuracy (5 neighbrs): ",metrics.accuracy_score(y_test,y_pred))

#generating model for k=7
#create KNN Classifier
knn = KNeighborsClassifier(n_neighbors=7)

#train the model using the training set
knn.fit(x_train, y_train)

#predict the responce for test dataset
y_pred = knn.predict(x_test)

#accuracy estimation
#model accuracy, how often is the classifier correct?
print("Accuracy (7 neighbrs): ",metrics.accuracy_score(y_test,y_pred))


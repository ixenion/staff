#               #   epochs - 10
#   TITANIC     #   accuracy - 0.77
#               #

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np                                  # optimised arrays
import pandas as pd                                 # data analytics tool
import matplotlib.pyplot as plt                     # visualisation of a graphs
#from IPython.display import clear_output           # specific for Tim's notebook
#from six.moves import urllib                       # and this

import tensorflow.compat.v2.feature_column as fc    
import tensorflow as tf



# load dataset
#dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv')   # train data
#dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv')     # testing data
dftrain = pd.read_csv('dataset/titanic_dftrain.csv')
dfeval = pd.read_csv('dataset/titanic_dfeval.csv')

y_train = dftrain.pop('survived')       # separate output data from input. y is output, the rest is input
y_eval = dfeval.pop('survived')
dftrain.drop('n_siblings_spouses', inplace=True, axis=1)
dftrain.drop('fare', inplace=True, axis=1)
dftrain.drop('embark_town', inplace=True, axis=1)
dftrain.drop('parch', inplace=True, axis=1)
dfeval.drop('n_siblings_spouses', inplace=True, axis=1)
dfeval.drop('fare', inplace=True, axis=1)
dfeval.drop('embark_town', inplace=True, axis=1)
dfeval.drop('parch', inplace=True, axis=1)
#print(dftrain.head())                   # prints first 5 lines
#print(dftrain["age"])                   # print only "age" column
#print(dftrain.loc[0], y_train.loc[0])   # print first row
#print(dftrain.describe())               # mean information
dftrain.shape                           # result - [rows, columns]


# data visualisation
dftrain.age.hist(bins=20)       # x - age, y - amount
dftrain.sex.value_counts().plot(kind='barh')    # two horisontal column from left to right
dftrain['class'].value_counts().plot(kind='barh')   # same but with class
pd.concat([dftrain, y_train], axis=1).groupby('sex').survived.mean().plot(kind='barh').set_xlabel('% survive')
# last is persentage survival by sex (male-20, female-78)


# handle categorical data
# translate it into a numbers
#categorical_columns = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck', 'embark_town', 'alone']
categorical_columns = ['sex', 'class', 'deck', 'alone']
#numeric_column = ['age', 'fare']
numeric_column = ['age']

feature_columns = []
for feature_name in categorical_columns:
    vocabulary = dftrain[feature_name].unique()     # gets a list of uniqe values from given feature column
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in numeric_column:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

#print(dftrain["embark_town"].unique())              # prints unque values



# Input function
# The tensorflow model requires that the data to be passed comes in as a tf.data.Dataset object.
# convert pandas dataframe into that object
def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
    def input_function():   # inner function, this will be returned
        ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data & its label
        if shuffle:
            ds = ds.shuffle(1000)   # randomize order of data
        ds = ds.batch(batch_size).repeat(num_epochs)    # split dataset into batches of 32 & repeate proess for number of epochs
        return ds           # return a batch of the dataset
    return input_function   # return a function objeect for use

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)


# creating model
# use linear estimator
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)            # train
result = linear_est.evaluate(eval_input_fn) # get model metrics/stats by testing on testing data

#clear_output()              # clear console utput
#print(result['accuracy'])   # the result variable is simply a dict of stats about our model


# get predictions from the model
result = list(linear_est.predict(eval_input_fn))    # list represents predictions
#print(result)

#print(result[0])    # look at one prediction
# access probabilities (survived or no)
#print(result[0]['probabilities'])       # [not surviving, surviving]

# print test input data & predicted output
print(dfeval.loc[0])                    # passenger info
print(y_eval.loc[0])                    # survived - 1
print('surviving chance: ',result[0]['probabilities'][1])    # prediction


########################
### user interaction ###
########################

dfheader = ['survived','sex','age','class','deck','alone']

# user inputs
#print('  -SURVIVED-')
#print('  available value:')
#vocabulary = dfevalfull['survived'].unique()
#for i in vocabulary:
#    print('  ', i)
survived = 1
#print(type(survived))
def uinput():
    global dfone, y_one
    print('  -GENDER-')
    print('  available value:')
    vocabulary = dftrain['sex'].unique()
    for i in vocabulary:
        print('  * ', i)
    sex = input('  -> ')
    print()

    print('  -AGE-')
    #print('  available value:')
    #vocabulary = dfevalfull['age'].unique()
    #for i in vocabulary:
    #    print('  ', i  )
    age = int(input('  -> '))
    print()

    print('  -CLASS-')
    print('  available value:')
    vocabulary = dftrain['class'].unique()
    for i in vocabulary:
        print('  * ', i)
    clas = input('  -> ')
    print()

    print('  -DECK-')
    print('  available value:')
    vocabulary = dftrain['deck'].unique()
    for i in vocabulary:
        print('  * ', i)
    deck = input('  -> ')
    print()

    print('  -ALONE-')
    print('  available value:')
    vocabulary = dftrain['alone'].unique()
    for i in vocabulary:
        print('  * ', i)
    alone = input('  -> ')
    print()

    dfone = pd.DataFrame([[survived, sex, age, clas, deck, alone]])
    dfone.to_csv('dataset/titanic_user_input.csv', index=False, header=dfheader)
    dfone = pd.read_csv('dataset/titanic_user_input.csv')
    y_one = dfone.pop('survived')
    #print(dfone.head(2))

while True:
    uinput()
    user_input_fn = make_input_fn(dfone, y_one, num_epochs=1, shuffle=False)
    result = linear_est.evaluate(user_input_fn) # get model metrics/stats by testing on testing data
    result = list(linear_est.predict(user_input_fn))    # list represents predictions
    print(dfone.loc[0])                    # passenger info
    print(y_one.loc[0])                    # survived - 1
    print('surviving chance: ',result[0]['probabilities'][1])    # prediction






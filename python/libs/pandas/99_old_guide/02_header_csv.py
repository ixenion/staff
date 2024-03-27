import pandas as pd

# change header
header = ['Survived',
          'PClass',
          'Full name',
          'Gender',
          'Age',
          'SibSp',
          'Parch',
          'TcktNumber',
          'Price',
          'Cabin',
          'DepStation']

titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv', names=header, skiprows=[0])
print(titanic_data.head(8888888888))

# replace header with numbers
titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv', header=None, skiprows=[0])

# cpecify delimeter
titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv', sep=';')



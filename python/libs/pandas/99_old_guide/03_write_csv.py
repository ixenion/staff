import pandas as pd

titanic_data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
#titanic_data.to_csv('titanic.csv')

# to get rid of the first unnamed colunm
titanic_data.to_csv('titanic.csv', index=False)

# change header
#new_header = ['', '', '', '']
#titanic_data.to_csv('titanic.csv', index=False, header=new_header)

# cucstom delimiter
titanic_data.to_csv('titanic.csv', index=False, sep=';')

# handling misisng values
titanic_data.to_csv('titanic.csv', index=False, na_rep='Unckown')






import pandas as pd

df = pd.read_csv('titanic.csv')

# how many female and male survived
result = df.groupby(['Sex', 'Survived'])['PassengerID'].count()
print(result)

# now see cabin class
result = df.groupby(['PClass', 'Survived'])['PassengerID'].count()
print(result)

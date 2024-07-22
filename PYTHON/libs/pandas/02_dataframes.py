import pandas as pd

# most iasier way to get df is from from a dictionary
my_dict = {
        'country':      ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
        'population':   [17.04, 143.5, 9.5, 45.5],
        'square':       [2724902, 17125191, 207600, 603628]
        }

df = pd.DataFrame(my_dict)
print(f"\nDataframe:\n{df}")

# get separate column
print(f"\nSeparate column:\n{df['country']}")

# det columns and indexes
print(f"\nDataframe columns:\n{df.columns}")
print(f"\nDataframe indexes:\n{df.index}")

# set index
df = pd.DataFrame(my_dict, index=['KZ', 'RU', 'BY', 'UA'])
# or on the fly
df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country code'

# access row by index
print(f"\nAccess DF by str index:\n{df.loc['KZ']}")
print(f"\nAccess DF by int index:\n{df.iloc[0]}")

# make selection by index and columns
result = df.loc[['KZ', 'RU'], 'population']
print(f"\nSelection by index and column:\n{result}")

# slicing
result = df.loc['KZ':'BY', :]
print(f"\nSelection by index and column with slicing:\n{result}")

# filtering
result = df[df.population > 10][['country', 'square']]
print(f"\nFiltering:\n{result}")

# dictionary and dot notation are the same
df.population
df['population']

# reset indexes
df.reset_index()


# When there are operations on DF, pandas returns new object DataFrame

# Let's add new column
df['density'] = df['population'] / df['square'] * 1_000_000
print(f"\nDF after creating new column 'density':\n{df}")

# remove column
df.drop(['density'], axis='columns')
# or
# del df['density']

# rename columns
df = df.rename(columns={'Country code': 'country_code'})

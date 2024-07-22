import pandas as pd

my_series = pd.Series([5, 6, 7, 8, 9])
print(f"Series example:\n{my_series}")

# get Series indexes and values
print(f"\nSeries indexes:\n{my_series.index}")
print(f"\nSeries values:\n{my_series.values}")

print(f"\nAccess elements by default indexes:\n{my_series[4]}")

# alter indexes
my_series2 = pd.Series([5, 6, 7, 8, 9], index=['a','b','c','d','e'])
print(f"\nAccess altered indexes;\n{my_series2['e']}")

# make a selection by several indexes and
print(f"\nSeveral indexes selection:\n{my_series2[['a','b','e']]}")
# group assignment.
my_series2[['a','b','e']] = 0
print(f"\nGroup assignment:\n{my_series2}")

# filter
print(f"\nFiltering:\n{my_series2[my_series2 > 0]}")
print(f"\nFiltering with math operations:\n{my_series2[my_series2 > 0]*2}")

# series as dictionary
my_dict = {'a': 5, 'b': 6, 'c': 7, 'd': 8}
my_series3 = pd.Series(my_dict)

# set series object name
my_series3.name = 'numbers'
# set series index name
my_series3.index.name = 'letters'

# change index on fly
my_series3.index = ['A', 'B', 'C', 'D']
print(f"\nChanged indexes on fly:\n{my_series3}")

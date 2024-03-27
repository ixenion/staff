# tutorial
# https://habr.com/ru/company/ruvds/blog/500426/

# data load
import pandas as pd

print('Downloading data...')
sales = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'sales')
states = pd.read_excel('https://github.com/datagy/mediumdata/raw/master/pythonexcel.xlsx', sheet_name = 'states')
print('Done!')

print(f"SALES:\n{sales.head()}")
print(f"STATES:\n{states.head()}")


# generate new column 'MoreThan500'
sales['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in sales['Sales']]


# delete column
sales.drop('MoreThan500', axis=1, inplace=True)
# or
# sales = sales.drop('MoreThan500', axis=1)


# join tables (VLOOKUP - join left)
print('\nLeft join')
sales1 = pd.merge(sales, states, how='left', on='City')
print(sales1.head())

print('\nRight join')
sales2 = pd.merge(sales, states, how='right', on='City')
print(sales2.head())

print('\nLeft_on, Right_on')
sales3 = pd.merge(sales, states, how='left', left_on='City', right_on='City')
print(sales3.head())


# Pivot tables
print('\nPivot tables')
pt = sales.pivot_table(index='City', values='Sales', aggfunc='sum')
print(pt)
print(pt['Sales'][0])

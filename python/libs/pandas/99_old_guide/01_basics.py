import pandas as pd

# create dataframe
df = pd.read_csv('https://raw.githubusercontent.com/jorisvandenbossche/pandas-tutorial/master/data/titanic.csv')
# get df type
type(df)
# check what's inside
print(df)

# OR create df from python dictionary
df2 = pd.DataFrame.from_dict({'a':[1,2],'b':[3,4]})

# save df to csv
#df.to_csv('./tmp.csv')

############################
# PRIMARY DATAFRAME ANALYS #
############################

# get common df info: entry(rows) number, columns description, column data type
df.info()

# get df shape
df.shape
# get df columns name
df.columns

# get first three entry
df.head(3)
# get last three entry
df.tail(3)
# get column datatype
df.dtypes


###############################
# ONE-DIMENTIONAL DATA/SERIES #
###############################

# filtering by column name
df['Name']
# curious fact
type(df['Name'])    # -> Series type (not DataFrame)
# get several columns
#df['Name', 'Age'] # error

# filtering by rows and columns
# get several columns and particular rows (5,10,15)
df.loc[[5,10,15],['Name','Age']]
# same as above but columns are indexes (not columns names)
df.iloc[[5,10,15],[0,1]]
# get 5-10 rows and 0-2 columns
df.iloc[5:11, :3]

# filtering by Boolean mask
# get all passengers which age is above 18
print(df[df['Age'] < 10 ])  # that's bool mask
# compare to list of objects
df[df['Age'].isin([5,10,15])]  # that's bool mask
# same as above
df[(df['Age'] == 5) | (df['Age'] == 10)]

# check that etry present
df['Name'].notna()
# dataframe filtered so that NA (Age) are excluded
df[df['Age'].notna()]
# also there is "isna"
# count NA by age
df['Age'].isna().sum()

# get all Names which age are known
df.loc[df['Age'].notna(), 'Name']


################
# DATA SORTING #
################




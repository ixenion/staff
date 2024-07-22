import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

# pandas aggregation options
# 1. list
result = df['fare'].agg(['sum', 'mean'])
print(result)

# 2. dictionary
result = df.agg({
        'fare': ['sum', 'mean'],
        'sex':  ['count']
            })
print(result)

# 3. tuple
result = df.agg(
        fare_sum=('fare', 'sum'),
        fare_mean=('fare', 'mean'),
        sex_count=('sex', 'count')
        )

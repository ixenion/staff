import pandas as pd
import seaborn as sns


df = sns.load_dataset('titanic')

# The most common built in aggregation functions are basic math functions
# including: sum, mean, median, minimum, maximum, standart deviation, variance,
# mean absolute deviation, product

# Mean Absolute Deviation - FutureWarning: The 'mad' method is deprecated and
# will be removed in a future version.
# To compute the same result, you may do '(df - df.mean()).abs().mean()'.

agg_func_math = {
        'fare': ['sum', 'mean', 'median', 'min', 'max', 'std', 'var', 'prod']
        }
result = df.groupby(['embark_town']).agg(agg_func_math).round(2)
print(result)

# One other useful shortcut is to use 'describe' to run multiple build-in
# aggregation at one time
agg_func_describe = {'fare': ['describe']}
result = df.groupby(['embark_town']).agg(agg_func_describe).round(2)
print(result)


# COUNTING


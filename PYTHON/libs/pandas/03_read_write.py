import pandas as pd

# there are several formats, that pandas supprots:

# read_clipboard, read_csv, read_exel, read_fwf,
# read_gbq, read_hdf, read_html, read_json, read_mgspack...

my_dict = {
        'country':      ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
        'population':   [17.04, 143.5, 9.5, 45.5],
        'square':       [2724902, 17125191, 207600, 603628]
        }

df = pd.DataFrame(my_dict)

# save to csv
df.to_csv('filename.csv')
# define separator
df.to_csv('filename.csv', sep=',')

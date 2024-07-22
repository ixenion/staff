d = {'10':1, '20':2}

for i in d:
    print(i)

try:
    d['ac']
except KeyError:
    print(f'Dict has no such key')

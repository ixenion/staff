r = csv.reader(open('testin.csv'))
lines = list(r)

#modifying:
lines[2][1] = '30'

# save
writer = csv.writer(open('testout.csv', 'w'))
writer.writerows(lines)

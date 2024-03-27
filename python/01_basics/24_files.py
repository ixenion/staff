import csv
from os import path

# read content:
file = path.join('zz_etc', 'point_24_files', 'file.txt')
a = open(file,"r")
f = a.read()
a.close()
#print(f)#print content o the file.txt row by row
correct = []
correct.append(int(f[6]))
#print(correct)
#print(f[6])


# write matrix to csv
marray = [[11,12],[21,22],[31,32]]
print(marray)
file = path.join('zz_etc', 'point_24_files', 'marray.csv')
with open(file,"w") as f:
    writer = csv.writer(f)
    writer.writerows(marray)
# read mattrix from csv
with open(file) as f:
    reader = csv.reader(f)
    data = list(reader)
print("")
print(data[1][0])

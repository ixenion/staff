

f1 = [1,2,3]
f2 = [4,6]
f3 = [[]for i in range(3)]



'''
for i in range(3):
    #print(i)
    f3[i].append(f1[i])
    f3[i].append(f2[i])
'''
#print(f3)

f3=zip(f1,f2)


for num, ai in enumerate(f3):
    print(ai[0],' ',ai[1])

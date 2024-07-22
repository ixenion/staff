numbs = [1, 2, 2, 5, 4, 7, 2, 1, 8, 23, 2]
num = numbs.copy()
numbs.sort()
i = 0
while i < len(numbs[:-2]):
    print(i)
    if numbs[i] == numbs[i+1]:
        numbs.remove(numbs[i+1])
        print(numbs)
        i = i - 1
        print(f"second i: {i}")
    i += 1
print(numbs)

############################################
#another way:
uniques = []
for number in num:
    if number not in uniques:
        uniques.append(number)
print(uniques)

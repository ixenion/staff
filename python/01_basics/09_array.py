#or list of lists

matrix = [
        [1, 2, 3],
        [4, 5, 7],
        [0, 9, 8]
        ]
# matrix[0] returns line 1 2 3
# matrix[0][1] ret. number 2

#print all numbers one by one
for row in matrix:
    for i in row:
        print(i)

# generate empty matrix
matrix = [[0]*2 for i in range(3)]
#for row in matrix:
#    for i in row:
#        matrix[row][i] = int(matrix[row][i])

print(matrix[0][0]/1)
print
matrix[0][0] = 22
print matrix

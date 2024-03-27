#number = [10, 3, 6, 2]
#max  number[0]
#for number in numbers:
#    if number > max:
#        max = number
#print(max)

def find_max(numbers):
    maxs = numbers[0]
    for number in numbers:
        if number > maxs:
            maxs = number
    return maxs



#convert.py contains:

#def lbs_to_kg(weight):
#    return weight * 0.45
#
#def kg_to_lbs(weight):
#    return weight / 0.45

from zz_etc.point_17_import import convert

print(convert.kg_to_lbs(70))
print(convert.lbs_to_kg(150))

from zz_etc.point_17_import.convert import kg_to_lbs

print(kg_to_lbs(100))

#################################################33
##example##
#reuse next code with import (find_max)

#number = [10, 3, 6, 2]
#max  number[0]
#for number in numbers:
#    if number > max:
#        max = number
#print(max)

from zz_etc.point_17_import.utils import find_max

numbers = [1, 3, 2, 5, 4]
maxs = find_max(numbers)
#print(maxs)
print(max(numbers))#max is already exists function with same purpose


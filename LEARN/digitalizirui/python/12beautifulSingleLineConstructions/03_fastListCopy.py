numbers = [1, 2, 3]
# not copy. when modifying "another_number", "number" will changed too
another_number = numbers

# most easy way to really copy. "another_number" now will be second list
another_numbers = numbers[:]

# copy list? but in reverse order
n2 = numbers[::-1]



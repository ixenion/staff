# Usual way:
numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)


# List comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)

# or spiskovie vklychenia

# basics
numbers = [i for i in range(10)]
print(numbers)


# Modifying a List with a List Comprehension If Else Statement
# new_list = [expression (if-else statement) for item in iterable]
old_list = [1,2,3,4,5]
new_list = ['even' if x % 2 == 0 else 'odd' for x in old_list]
print(new_list)


# Filtering a List with List Comprehension If Statement
# new_list = [expression for item in iterable (if statement)]
old_list = [1,2,3,4,5]
new_list = [x for x in old_list if x % 2 == 1]
print(new_list)


# Multiple If Conditions in List Comprehensions
# Let’s take a look at an example. If we wanted to generate a list of numbers
# that are divisible by 2 and by 5, we could do this with a for-loop:
new_list = []
for i in range(1, 101):
    if i % 2 == 0:
        if i % 5 == 0:
            new_list.append(i)
print(new_list)

# To do this with a list comprehension,
# we can cut down the amount of code significantly:
new_list = [i for i in range(1, 101) if i % 2 == 0 if i % 5 == 0]
print(new_list)


# Nested List Comprehensions
# If we wanted to reduce this to a flattened list, we could do this with a for-loop:
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = []
for _list in nested_list:
	for item in _list:
		flat_list.append(item)
print(flat_list)

# To do this with a list comprehension, we can write:
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [item for _list in nested_list for item in _list]
print(flat_list)


# Finding Common Items in Two Lists Using List Comprehensions
# Let’s first see how this can be done using for-loops:
list1 = ['apple', 'orange', 'banana', 'grape']
list2 = ['grapefruit', 'apple', 'grape', 'pear']
common_items = []

for i in list1:
	for j in list2:
		if i == j:
			common_items.append(j)
print(common_items)

# To do this using a list comprehension, we can simply write:
list1 = ['apple', 'orange', 'banana', 'grape']
list2 = ['grapefruit', 'apple', 'grape', 'pear']

common_items = [item for item in list1 if item in list2]
print(common_items)

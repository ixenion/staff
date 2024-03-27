list = [2, 3, 6, 110, 5]
max_from_list = list[0]
for i in list[1:]:
    if i > max_from_list:
        max_from_list = i
print(f"Max is {max_from_list}")

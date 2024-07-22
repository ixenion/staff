for item in 'Python':
    print(item)

for item in ['Mosh', 'John']:#        [1, 2, 3, 4]
    print(item)

for item in range(10):# range from 0 to 9. range(5, 10): from 5 to 9
    print(item)

#for item in range(5, 10, 2):# output 5 7 9

price = [10, 20, 30]
total_cost = 0
for item in price:
    total_cost += item
print(f"total: {total_cost}")

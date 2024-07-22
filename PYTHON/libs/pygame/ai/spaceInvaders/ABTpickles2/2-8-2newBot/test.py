from random import choices
population = [0, 1, 2]
weights = [0.25, 0.25, 0.5]

for i in range(6):
    print(choices(population, weights))

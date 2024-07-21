from random import choices

population = [1, 2, 3, 4, 5, 6]
weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]

print(choices(population, weights))

# The optional keyword-only argument k allows
# one to request more than one sample at once.
million_samples = choices(population, weights, k=10**6)
from collections import Counter
print(Counter(million_samples))

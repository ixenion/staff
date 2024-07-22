import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [3.1, 2.1, 8.7, 0.3],
           [3, 2, 8, 1]]

biases = [2, 3, 0.5]


output = np.dot(weights, inputs) + biases
print(output)

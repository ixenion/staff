#more then one input sets
import numpy as np

x = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class Layer_dence:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.rand(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_dence(4,5)
layer2 = Layer_dence(5,2)

layer1.forward(x)
#print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)

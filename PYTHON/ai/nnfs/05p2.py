import numpy as np
import nnfs
from nnfs.datasets import spiral_data
# see for code: https://gist.github.com/Sentdex/454cb20ec5acf0e76ee8ab8448e6266cc

nnfs.init()

X, y = spiral_data(100, 3)


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
#        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.weights = np.random.normal(0.0, pow(n_inputs, -0.5), (n_inputs, n_neurons))
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(2,5)
activation1 = Activation_ReLU()

layer1.forward(X)

print(layer1.output[200])
activation1.forward(layer1.output)
print(activation1.output[200])


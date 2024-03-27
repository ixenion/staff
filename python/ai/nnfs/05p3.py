import numpy as np

np.random.seed(0)

# sample dataset
def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.05
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

# dense layer
class Layer_Dense:
    def __init__(self, inputs, neurons):
        #self.weights = 0.01 * np.random.randn(inputs, neurons)
        self.weights = np.random.normal(0.0, pow(inputs, -0.5), (inputs, neurons))
        self.biases = np.zeros((1, neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

# ReLU activation
class Activation_ReLU:
    # forward pass
    def forward(self, inputs):
        self.output = np.maximum(0,inputs)

# soft ativation
class Activation_Softmax:
    # forward pass
    def forward(self, inputs):
        # get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # normalized them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

# create dataset
X, y = create_data(100,3)

# create layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,3)# 2 inputs because each sample has 2 features, 3 outputs

# create ReLU activation
activation1 = Activation_ReLU()

# create second dense layer with 3 input features (as we take output of previous layer here) and 3 output values (output valus)
dense2 = Layer_Dense(3,3)

# create softmax activation function
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])


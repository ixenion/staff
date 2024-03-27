import numpy as np
#import math
import random

random.seed(0)
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
        self.weights = 0.01 * np.random.randn(inputs, neurons)
        #self.weights = np.random.normal(0.0, pow(inputs, -0.5), (inputs, neurons))
        self.biases = np.zeros((1, neurons))
    
    # forward pass
    def forward(self, inputs):
        # remember input walues
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases

    # backward pass
    def backward(self, dvalues):
        # gradient on parameters
        self.dweights = np.dot(self.inputs.T, dvalues)
        self.dbiases = np.sum(dvalues, axis=0, keepdims=True)
        # gradient on values
        self.dvalues = np.dot(dvalues, self.weights.T)

# ReLU activation
class Activation_ReLU:
    # forward pass
    def forward(self, inputs):
        # remember input values
        self.inputs = inputs
        # calculate output values from input one
        self.output = np.maximum(0,inputs)

    # backward pass
    def backward(self, dvalues):
        # sine we need to modify original variable,
        # let's make a copy of values first
        self.dvalues = dvalues.copy()

        # zero gradient where input values were negative
        self.dvalues[self.inputs <= 0] = 0

# soft ativation
class Activation_Softmax:
    # forward pass
    def forward(self, inputs):
        # remember input values
        self.inputs = inputs
        # get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # normalized them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

    # backward pass
    def backward(self, dvalues):
        self.dvalues = dvalues.copy()

# Cross-entropy loss
class Loss_CategoricalCrossentropy:
    # forward pass
    def forward(self, y_pred, y_true):
        # number of samples in a batch
        samples = y_pred.shape[0]
        # probabilities for target values - only if categorical labels
        if len(y_true.shape) == 1:
            y_pred = y_pred[range(samples), y_true]
        # losses
        negative_log_likelihoods = -np.log(y_pred)
        # mask values - only for one-hot encoded labels
        if len(y_true.shape) == 2:
            negative_log_likelihoods *= y_true
        # overall loss
        data_loss = np.sum(negative_log_likelihoods) / samples
        return data_loss

    # backward pass
    def backward(self, dvalues, y_true):
        samples = dvalues.shape[0]
        self.dvalues = dvalues.copy()  # copy so we can safely modify
        self.dvalues[range(samples), y_true] -= 1
        self.dvalues = self.dvalues / samples

# stochastic gradient desent (SGD)
class Optimizer_sgd:
    # init optimizer - set settings,
    # learn. rate of 1. is default for this optimizer
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    # update params
    def update_params(self, layer):
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases

# create dataset
X, y = create_data(100,3)

# create layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,64)# 2 inputs because each sample has 2 features, 3 outputs

# create ReLU activation
activation1 = Activation_ReLU()

# create second dense layer with 3 input features (as we take output of previous layer here) and 3 output values (output valus)
dense2 = Layer_Dense(64,3)

# create softmax activation function
activation2 = Activation_Softmax()

# create loss funtion
loss_function = Loss_CategoricalCrossentropy()

# create optimizer
optimizer = Optimizer_sgd()

# forward pass
dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

loss = loss_function.forward(activation2.output, y)

print('loss: ',loss)

# calculate accuracy from output of activation2 and targets
predictions = activation2.output[range(len(activation2.output)), y]
#print('pred1: \n',predictions)
predictions = np.argmax(activation2.output, axis=1)
#print('pred2: \n',predictions)
accuracy = np.mean(predictions==y)
print('acc: ',accuracy)

# backward pass
loss_function.backward(activation2.output, y)
activation2.backward(loss_function.dvalues)
dense2.backward(activation2.dvalues)
activation1.backward(dense2.dvalues)
dense1.backward(activation1.dvalues)

# use optimizer to update weights
optimizer.update_params(dense1)
optimizer.update_params(dense2)

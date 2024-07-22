# SGD with momentum (stochastic gradient ddesent optimizer)           |
# learning rate - lineary decreases                                   |   L1 and L2 regularization added
# with                                                                |_____________________________________
# decay = 5e-8  momentum = 0.9  lr = default  epoch = 10.000          |
# final result                                                        |
# accuracy = 0.860  loss = 0.4  lr = 0.086                            |
# acc. and loss kinda randomly bhavioring ?!                          |
#                                                                     |
#                                                                     |
# AdaGrad (Adaptive Gradient - SGD mod)                               |
# learning rate - unic for each weight (?)                            |
# with                                                                |
# decay = 1e-8  epsilon = 1e-7  lr = deault  epoch = 10.000           |
# final result                                                        |
# accuracy = 0.980-0.990  loss = 0.090-0.05  lr = 0.6126359931347328  |
#
#
# RMSProp (Root Mean Square Propagation)
# similar to AdaGrad but math is differ
# with
# decay = 4e-8  lr = 0.05  rho = 0.999  epoch = 10.000
# final result
# accuracy = 0.980-0.990  loss = 0.095-0.04  lr = 0.007044


# Adam (Adaptive moment)
# built atop RMSprop + momentum
# with
# decay = 1e-8  lr = 0.05  rho = 0.999  momentum = 0.9  epoch = 3.000
# final result
# accuracy = 0.980  loss = 0.07  lr = 0.047


import numpy as np
import random
#import math

#random.seed(0)
#np.random.seed(0)

##############################################################################################
##########################################   CLASSES   #######################################
##############################################################################################

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
    def __init__(self, inputs, neurons, weight_regularizer_l1=0, weight_regularizer_l2=0, bias_regularizer_l1=0, bias_regularizer_l2=0):
        self.weights = 0.01 * np.random.randn(inputs, neurons)
        #self.weights = np.random.normal(0.0, pow(inputs, -0.5), (inputs, neurons))
        self.biases = np.zeros((1, neurons))
        # set regularization strength
        self.weight_regularizer_l1 = weight_regularizer_l1
        self.weight_regularizer_l2 = weight_regularizer_l2
        self.bias_regularizer_l1 = bias_regularizer_l1
        self.bias_regularizer_l2 = bias_regularizer_l2
    
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
        
        # gradients on regularization
        # L1 on weights
        if self.weight_regularizer_l1 > 0:
            dL1 = self.weights.copy()
            dL1[dL1 >= 0] = 1
            dL1[dL1 < 0] = -1
            self.dweights += self.weight_regularizer_l1 * dL1
        # L2 on weights
        if self.weight_regularizer_l2 > 0:
            self.dweights += 2 * self.weight_regularizer_l2 * self.weights
        # L1 on biases
        if self.bias_regularizer_l1 > 0:
            dL1 = self.biases.copy()
            dL1[dL1 >= 0] = 1
            dL1[dL1 < 0] = -1
            self.dbiases += self.bias_regularizer_l1 * dL1
        # L2 on biases
        if self.bias_regularizer_l2 > 0:
            self.dbiases += 2 * self.bias_regularizer_l2 * self.biases

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

# softmax ativation
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

# common loss class
class Loss:

    # regularization loss calculation
    def regularization_loss(self, layer):
        # 0 by default
        regularization_loss = 0

        # L1 regularization - weights
        if layer.weight_regularizer_l1 > 0:  # calculate only when factor greater than 0
            regularization_loss += layer.weight_regularizer_l1 * np.sum(np.abs(layer.weights))

        # L2 regularization - weights
        if layer.weight_regularizer_l2 > 0:
            regularization_loss += layer.weight_regularizer_l2 * np.sum(layer.weights * layer.weights)

        # L1 regularization - biases
        if layer.bias_regularizer_l1 > 0:  # calculate only when factor greater than 0
            regularization_loss += layer.bias_regularizer_l1 * np.sum(np.abs(layer.biases))

        # L2 regularization - biases
        if layer.bias_regularizer_l2 > 0:
            regularization_loss += layer.bias_regularizer_l2 * np.sum(layer.biases * layer.biases)

        return regularization_loss

# Cross-entropy loss
class Loss_CategoricalCrossentropy(Loss):
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
        dvalues = dvalues.copy()  # copy so we can safely modify
        dvalues[range(samples), y_true] -= 1
        dvalues = dvalues / samples
        self.dvalues = dvalues

# stochastic gradient desent (SGD)
class Optimizer_SGD:

    # init optimizer - set settings,
    # learn. rate of 1. is default for this optimizer
    def __init__(self, learning_rate=1.0, decay=0., momentum=0., nesterov=False):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.momentum = momentum
        self.nesterov = nesterov
    
    # call once before any params updates
    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.current_learning_rate * (1. / (1. + self.decay * self.iterations))
    
    # update params
    def update_params(self, layer):
        # if layer does not contain momentum arrays, create them
        # filled with zeros
        if not hasattr(layer, 'weight_momentums'):
            layer.weight_momentums = np.zeros_like(layer.weights)
            layer.bias_momentums = np.zeros_like(layer.biases)

        # if we use momentum
        if self.momentum:
            # build weight updates with momentum - take previous
            # updates multiplied by retain factor an update with ccurr gradients
            weight_updates = (
                    (self.momentum * layer.weight_momentums) -
                    (self.current_learning_rate * layer.dweights)
                    )
            layer.weight_momentums = weight_updates
            # build bias updates
            bias_updates = (
                    (self.momentum * layer.bias_momentums) -
                    (self.current_learning_rate * layer.dbiases)
                    )
            layer.bias_momentums = bias_updates
            
            # apply Nesterov as well?
            if self.nesterov:
                weight_updates = self.momentum * weight_updates - self.current_learning_rate * layer.dweights
                bias_updates = self.momentum * bias_updates - self.current_learning_rate * dbiases
        
        # vanilla SGD updates (as before momentum updates)
        else:
            weight_updates = -self.current_learning_rate * layer.dweights
            bias_updates = -self.current_learning_rate * layer.dbiases

        layer.weights += weight_updates
        layer.biases += bias_updates
    
    # call once after any params updates
    def post_update_params(self):
        self.iterations += 1

# AdaGrad optimizer class
class Optimizer_AdaGrad:

    # init optimizer - set settings,
    def __init__(self, learning_rate=1.0, decay=0., epsilon=1e-7):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon

    # call once before any params updates
    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.current_learning_rate * (1. / (1. + self.decay * self.iterations))
    
    # update params
    def update_params(self, layer):
        # if layer does not contain cache arrays, create them
        # filled with zeros
        if not hasattr(layer, 'weight_cache'):
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache = np.zeros_like(layer.biases)
        
        # update cache with squared current gradients
        layer.weight_cache += layer.dweights**2
        layer.bias_cache += layer.dbiases**2
        
        # vanilla SGD params update +
        # normalization with square rooted cache
        layer.weights += -self.current_learning_rate * layer.dweights / (np.sqrt(layer.weight_cache) + self.epsilon)
        layer.biases += -self.current_learning_rate * layer.dbiases / (np.sqrt(layer.bias_cache) + self.epsilon)
    
    # call once after any params updates
    def post_update_params(self):
        self.iterations += 1

# RMSProp optimizer class
class Optimizer_RMSProp:

    # init optimizer - set settings,
    def __init__(self, learning_rate=0.001, decay=0., epsilon=1e-7, rho=0.9):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon
        self.rho = rho

    # call once before any params updates
    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.current_learning_rate * (1. / (1. + self.decay * self.iterations))

    # update params
    def update_params(self, layer):
        # if layer does not contain cache arrays, create ones
        # filled with zeros
        if not hasattr(layer, 'weight_cache'):
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache = np.zeros_like(layer.biases)
        
        # update cache with squared current gradients
        layer.weight_cache = self.rho * layer.weight_cache + (1 - self.rho) * layer.dweights**2
        layer.bias_cache = self.rho * layer.bias_cache + (1 - self.rho) * layer.dbiases**2

        # vanilla SGD params update +
        # normalization with square rooted cache
        layer.weights += -self.current_learning_rate * layer.dweights / (np.sqrt(layer.weight_cache) + self.epsilon)
        layer.biases += -self.current_learning_rate * layer.dbiases / (np.sqrt(layer.bias_cache) + self.epsilon)

    # call once after any params updates
    def post_update_params(self):
        self.iterations += 1

# Adam optimizer class
class Optimizer_Adam:

    # init optimizer - set settings,
    def __init__(self, learning_rate=0.001, decay=0., epsilon=1e-7, momentum=0.9, rho=0.999):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon
        self.rho = rho
        self.momentum = momentum

    # call once before any params updates
    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.current_learning_rate * (1. / (1. + self.decay * self.iterations))

    # update params
    def update_params(self, layer):
        # if layer does not contain cache arrays, create ones
        # filled with zeros
        if not hasattr(layer, 'weight_cache'):
            layer.weight_momentums = np.zeros_like(layer.weights)
            layer.bias_momentums = np.zeros_like(layer.biases)
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_cache = np.zeros_like(layer.biases)
        
        # update momentum with current gradients
        layer.weight_momentums = self.momentum * layer.weight_momentums + (1 - self.momentum) * layer.dweights
        layer.bias_momentums = self.momentum * layer.bias_momentums + (1 - self.momentum) * layer.dbiases
        
        # get correct momentum
        # self.iteration is 0 at first pass
        # and we need to start with 1 here
        weight_momentums_corrected = layer.weight_momentums / (1 - self.momentum ** (self.iterations + 1))
        bias_momentums_corrected = layer.bias_momentums / (1 - self.momentum ** (self.iterations + 1))

        # update cache with squared current gradients
        layer.weight_cache = self.rho * layer.weight_cache + (1 - self.rho) * layer.dweights**2
        layer.bias_cache = self.rho * layer.bias_cache + (1 - self.rho) * layer.dbiases**2

        # get corrected bias
        weight_cache_corrected = layer.weight_cache / (1 - self.rho ** (self.iterations + 1))
        bias_cache_corrected = layer.bias_cache / (1 - self.rho ** (self.iterations + 1))

        # vanilla SGD params update +
        # normalization with square rooted cache
        layer.weights += -self.current_learning_rate * weight_momentums_corrected / (np.sqrt(weight_cache_corrected) + self.epsilon)
        layer.biases += -self.current_learning_rate * bias_momentums_corrected / (np.sqrt(bias_cache_corrected) + self.epsilon)

    # call once after any params updates
    def post_update_params(self):
        self.iterations += 1

#############################################################################################
##########################################   MAIN   #########################################
#############################################################################################

# create dataset
X, y = create_data(100,3)

# create layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,64, weight_regularizer_l2=1e-5, bias_regularizer_l2=1e-5)# 2 inputs because each sample has 2 features, 3 outputs

# create ReLU activation
activation1 = Activation_ReLU()

# create second dense layer with 3 input features (as we take output of previous layer here) and 3 output values (output valus)
dense2 = Layer_Dense(64,3)

# create softmax activation function
activation2 = Activation_Softmax()

# create loss funtion
loss_function = Loss_CategoricalCrossentropy()
loss_function2 = Loss()

# create optimizer
#optimizer = Optimizer_AdaGrad(decay=1e-8)
#optimizer = Optimizer_SGD(decay=5e-8, momentum=0.9)
#optimizer = Optimizer_RMSProp(learning_rate=0.05, decay=4e-8, rho=0.999)
optimizer = Optimizer_Adam(learning_rate=0.05, decay=1e-8, momentum=0.9, rho=0.999)

# train in loop
for epoch in range(1000):
    # forward pass
    dense1.forward(X)
    activation1.forward(dense1.output)

    dense2.forward(activation1.output)
    activation2.forward(dense2.output)

    data_loss = loss_function.forward(activation2.output, y)
    
    # calculate regularization penalty
    regularization_loss = loss_function2.regularization_loss(dense1) + loss_function2.regularization_loss(dense2)
    # calculate overall loss
    loss = data_loss + regularization_loss

    # calculate accuracy from output of activation2 and targets
    #predictions = activation2.output[range(len(activation2.output)), y]
    predictions = np.argmax(activation2.output, axis=1)
    #print('pred2: \n',predictions)
    accuracy = np.mean(predictions==y)
    #print('acc: ',accuracy)
    if not epoch % 100:
        #print('epoch:',epoch, ' acc:',accuracy, ' loss:',loss)
        print(f'epoch: {epoch}, acc: {accuracy:.3f}, loss: {loss:.3f}, data_loss: {data_loss:.3f}, reg_loss: {regularization_loss:.3}, lr: {optimizer.current_learning_rate}')

    # backward pass
    loss_function.backward(activation2.output, y)
    activation2.backward(loss_function.dvalues)
    dense2.backward(activation2.dvalues)
    activation1.backward(dense2.dvalues)
    dense1.backward(activation1.dvalues)

    # use optimizer to update weights
    optimizer.pre_update_params()
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)
    optimizer.post_update_params()

# validate model
# create test dataset
X_test, y_test = create_data(100, 3)

# make a forward pass of our test data thru NN
dense1.forward(X_test)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)

loss = loss_function.forward(activation2.output, y_test)
predictions = np.argmax(activation2.output, axis=1)
accuracy = np.mean(predictions==y_test)

print('')
print('test acc:',accuracy, ' loss:',loss)


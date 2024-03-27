# SGD with momentum (stochastic gradient ddesent optimizer)           |
# learning rate - lineary decreases                                   |   L1 and L2 regularization added
# with                                                                |_____________________________________
# decay = 5e-8  momentum = 0.9  lr = default  epoch = 10.000          |
# final result                                                        |   Dropout initialized
# accuracy = 0.860  loss = 0.4  lr = 0.086                            |_____________________________________
# acc. and loss kinda randomly bhavioring ?!                          |
#                                                                     |   Binary Logistic Regression
#                                                                     |   +
# AdaGrad (Adaptive Gradient - SGD mod)                               |   Sigmoid activation function
# learning rate - unic for each weight (?)                            |_____________________________________
# with                                                                |
# decay = 1e-8  epsilon = 1e-7  lr = deault  epoch = 10.000           |   New sin dataset
# final result                                                        |   +
# accuracy = 0.980-0.990  loss = 0.090-0.05  lr = 0.6126359931347328  |   Regression NN
#                                                                     |   (output is one neuron, which meaning is predicted number)
#                                                                     |_____________________________________
# RMSProp (Root Mean Square Propagation)                              |
# similar to AdaGrad but math is differ                               |
# with                                                                |
# decay = 4e-8  lr = 0.05  rho = 0.999  epoch = 10.000                |
# final result                                                        |
# accuracy = 0.980-0.990  loss = 0.095-0.04  lr = 0.007044            |


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
def create_sin_data(samples=10000):
   X = np.arange(samples).reshape(-1, 1) / samples
   y = np.sin(2 * np.pi * X).reshape(-1, 1)
   return X, y

def create_spiral_data(points, classes):
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.05
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y

##########################   layers   ##########################
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
        # gradient on values
        self.dvalues = np.dot(dvalues, self.weights.T)

# Dropout
class Layer_Dropout:
    #init
    def __init__(self, rate):
        self.rate = 1 - rate

    # forward pass
    def forward(self, values):
        # save input values
        self.input = values

        self.binary_mask = np.random.binomial(1, self.rate, size=values.shape) / self.rate
        # apply mask to output values
        self.output = values * self.binary_mask

    # backward pass
    def backward(self, dvalues):
        # gradient on values
        self.dvalues = dvalues * self.binary_mask

##########################   activation functions   ##########################
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

# sigmoid activation
class Activation_Sigmoid:

    # forward pass
    def forward(self, inputs):
        # save input and calculate/save output of the sigmoid ffunction
        self.input = inputs
        self.output = 1 / (1 + np.exp(-inputs))

    # backward pass
    def backward(self, dvalues):
        # derivative - calculates from output of the sigmoid function
        self.dvalues = dvalues * (1 - self.output) * self.output

# linear activation
class Activation_Linear:
    # forward pass
    def forward(self, inputs):
        # just remember values
        self.input = inputs
        self.output = inputs
    #backward pass
    def backward(self, dvalues):
        # 1 is derivative, 1 * dvalues = dvalues - chain rule
        self.dvalues = dvalues.copy()

##########################   losses   ##########################
# common loss class
class Loss:

    # regularization loss calculation
    def regularization_loss(self, layer):
        # 0 by default
        regularization_loss = 0.0

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
        #data_loss = np.sum(negative_log_likelihoods) / samples
        #return data_loss
        return negative_log_likelihoods

    # backward pass
    def backward(self, dvalues, y_true):
        samples = dvalues.shape[0]
        dvalues = dvalues.copy()  # copy so we can safely modify
        dvalues[range(samples), y_true] -= 1
        dvalues = dvalues / samples
        self.dvalues = dvalues

# binary cross-entropy loss
class Loss_BinaryCrossentropy(Loss):

    # forward pass
    def forward(self, y_pred, y_true):
        # clip data to prevent division by 0
        # clip both sides to not drag mean towards any value
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # calculate sample-wise loss
        sample_losses = -(y_true * np.log(y_pred_clipped) + (1 - y_true) * np.log(1 - y_pred_clipped))

        # return losses
        return sample_losses

    # backward pass
    def backward(self, dvalues, y_true):
        # clip data to prevent division by 0
        # clip both sides to not drag mean towards any value
        clipped_dvalues = np.clip(dvalues, 1e-7, 1 - 1e-7)

        # gradient on values
        self.dvalues = -(y_true / clipped_dvalues - (1 - y_true) / (1 - clipped_dvalues))
        #self.dvalues = -(y_true / dvalues - (1 - y_true) / (1 - dvalues))

# mean squared error loss
class Loss_MeanSquaredError(Loss):  #L2 loss

    # forward pass
    def forward(self, y_pred, y_true):
        #calculate loss
        data_loss = 2 * np.mean((y_true - y_pred)**2, axis=-1)
        # retrn losses
        return data_loss

    # backward pass
    def backward(self, dvalues, y_true):
        # gradient on values
        self.dvalues = -2 * (y_true - dvalues)# or -2 ?

# mean absolute error
class Loss_meanAbsoluteError(Loss):  #L1 loss

    # forward pass
    def forward(self, y_pred, y_true):
        # calculate loss
        data_loss = np.mean(np.abs(y_true - y_pred), axis=-1)
        # return losses
        return data_loss

    # backward pass
    def backward(self, dvalues, y_true):
        # gradient on values
        self.dvalues = - np.sign(y_true - dvalues)


##########################   optimizers   ##########################
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

        # get corrected cache
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
import time
# create dataset
#X, y = create_spiral_data(100,2)
X, y = create_sin_data(samples=3000)

# reshape albels to e a list of lists             --|
# inner list contains one output (either 0 or 1)    |  only for sigmoid output AF
# per each output neuron, 1 in this case            |
#y = y.reshape(-1,1)#                              --|

# create layer with 2 input features and 3 output values
dense1 = Layer_Dense(1,64, weight_regularizer_l2=0, bias_regularizer_l2=0)# 2 inputs because each sample has 2 features, 3 outputs

# create ReLU activation
activation1 = Activation_ReLU()

# create dropout layer
dropout1 = Layer_Dropout(0.0)
dropout2 = Layer_Dropout(0.0)

# create second dense layer with 3 input features (as we take output of previous layer here) and 3 output values (output valus)
dense2 = Layer_Dense(64,64)
activation2 = Activation_ReLU()

dense3 = Layer_Dense(64, 1)
activation3 = Activation_Linear()

# create loss funtion
#loss_function = Loss_BinaryCrossentropy()
#loss_funtion = Loss_CategoriaclCrossentropy()
loss_function = Loss_MeanSquaredError()
lf2 = Loss()

# create optimizer
#optimizer = Optimizer_AdaGrad(decay=1e-8)
#optimizer = Optimizer_SGD(decay=5e-8, momentum=0.9)
#optimizer = Optimizer_RMSProp(learning_rate=0.05, decay=4e-8, rho=0.999)
optimizer = Optimizer_Adam(learning_rate=0.001, decay=1e-8, momentum=0.9, rho=0.999)

# there are no really accuracy factor for regression problem,
# but we can simulate/aproximate it. We'll calculate it by checking
# how many values have a difference to their ground truth equivalent
# less than given precision
# WE'll calculate this precision as a fraction of standart deviation
# of all the ground truth values
accuracy_precision = np.std(y) / 500

# train in loop
for epoch in range(3001):
    #time.sleep(0.3)
    # forward pass
    dense1.forward(X)
    activation1.forward(dense1.output)
    dropout1.forward(activation1.output)
    dense2.forward(dropout1.output)
    activation2.forward(dense2.output)
    dropout2.forward(activation2.output)
    dense3.forward(dropout2.output)
    activation3.forward(dense3.output)


    #data_loss = loss_function.forward(activation2.output, y)# for categorical
    #sample_losses = loss_function.forward(activation2.output, y)# for binary
    sample_losses = loss_function.forward(activation3.output, y)# for regression
    data_loss = np.mean(sample_losses)# for binary and regression

    # calculate regularization penalty
    regularization_loss = lf2.regularization_loss(dense1) + lf2.regularization_loss(dense2) + lf2.regularization_loss(dense3)
    # calculate overall loss
    loss = data_loss + regularization_loss

    # calculate accuracy from output of activation2 and targets
    #predictions = activation2.output[range(len(activation2.output)), y]
    #predictions = np.argmax(activation2.output, axis=1)# for categorical
    #predictions = (activation2.output > 0.5) * 1#  for binary
    #print('pred2: \n',predictions)
    #accuracy = np.mean(predictions==y)#for binary (and ategorical ?)

    # regression only
    # to calculate it we are taking absolute difference between
    # preditions and ground truth values are compare if differences
    # are lower than given preccision value
    predictions = activation3.output
    accuracy = np.mean(np.absolute(predictions - y) < accuracy_precision)

    #print('acc: ',accuracy)
    if not epoch % 50:
        print(f'epoch: {epoch}, acc: {accuracy:.3f}, loss: {loss:.3f}, data_loss: {data_loss:.3f}, reg_loss: {regularization_loss:.3}, lr: {optimizer.current_learning_rate}')

    if not epoch % 50:
        print ("sleeping...")
        time.sleep(10)

    # backward pass
    loss_function.backward(activation3.output, y)
    activation3.backward(loss_function.dvalues)
    dense3.backward(activation3.dvalues)
    dropout2.backward(dense3.dvalues)
    activation2.backward(dropout2.dvalues)
    dense2.backward(activation2.dvalues)
    dropout1.backward(dense2.dvalues)
    activation1.backward(dropout1.dvalues)
    dense1.backward(activation1.dvalues)

    # use optimizer to update weights
    optimizer.pre_update_params()
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)
    optimizer.update_params(dense3)
    optimizer.post_update_params()

# validate model
# create test dataset
X_test, y_test = create_data(100, 2)

# reshape albels to e a list of lists             --|
# inner list contains one output (either 0 or 1)    |  only for sigmoid output AF
# per each output neuron, 1 in this case            |
y_test = y_test.reshape(-1,1)#                              --|

# make a forward pass of our test data thru NN
dense1.forward(X_test)
activation1.forward(dense1.output)
dense2.forward(activation1.output)
activation2.forward(dense2.output)

#loss = loss_function.forward(activation2.output, y_test)# for categorial
#predictions = np.argmax(activation2.output, axis=1)# for categorical
sample_losses = loss_function.forward(activation2.output, y_test)# for binary
loss = np.mean(sample_losses)# for binary
predictions = (activation2.output > 0.5) * 1# for binary
accuracy = np.mean(predictions==y_test)

print('')
print('validation acc:',accuracy, ' loss:',loss)


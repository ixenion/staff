# SGD with momentum (stochastic gradient descent optimizer)           |
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
# similar to AdaGrad but math is differ                               |   Model Object
# with                                                                |_______________________________________
# decay = 4e-8  lr = 0.05  rho = 0.999  epoch = 10.000                |
# final result                                                        |   Fashion dataset
# accuracy = 0.980-0.990  loss = 0.095-0.04  lr = 0.007044            |   +
#                                                                     |   batches
#                                                                     |
# Adam (Adaptive moment)                                              |
# built atop RMSprop + momentum                                       |
# with                                                                |
# decay = 1e-8  lr = 0.05  rho = 0.999  momentum = 0.9  epoch = 3.000 |
# final result
# accuracy = 0.980  loss = 0.07  lr = 0.047


import numpy as np
import random
import time
import os
import cv2

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
    def forward(self, inputs, training):
        # remember input walues
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases

    # backward pass
    def backward(self, dinputs):
        # gradient on parameters
        self.dweights = np.dot(self.inputs.T, dinputs)
        self.dbiases = np.sum(dinputs, axis=0, keepdims=True)
        # gradient on values
        self.dinputs = np.dot(dinputs, self.weights.T)
        
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
        self.dinputs = np.dot(dinputs, self.weights.T)

# Dropout
class Layer_Dropout:
    #init
    def __init__(self, rate):
        self.rate = 1 - rate

    # forward pass
    def forward(self, inputs, training):
        # save input values
        self.input = inputs
        # if not the training mode - return values
        if not training:
            self.output = inputs.copy
        
        # generate and save scaled mask
        self.binary_mask = np.random.binomial(1, self.rate, size=inputs.shape) / self.rate
        # apply mask to output values
        self.output = inputs * self.binary_mask

    # backward pass
    def backward(self, dinputs):
        # gradient on values
        self.dinputs = dinputs * self.binary_mask

##########################   activation functions   ##########################
# ReLU activation
class Activation_ReLU:
    # forward pass
    def forward(self, inputs, training):
        # remember input values
        self.inputs = inputs
        # calculate output values from input one
        self.output = np.maximum(0,inputs)

    # backward pass
    def backward(self, dinputs):
        # sine we need to modify original variable,
        # let's make a copy of values first
        self.dinputs = dinputs.copy()

        # zero gradient where input values were negative
        self.dinputs[self.inputs <= 0] = 0

    # calculate predictions for output
    def predictions(self, outputs):
        return outputs

# softmax ativation
class Activation_Softmax:
    # forward pass
    def forward(self, inputs, training):
        # remember input values
        self.inputs = inputs
        # get unnormalized probabilities
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        # normalized them for each sample
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

    # backward pass
    def backward(self, dinputs):
        self.dinputs = dinputs.copy()
    
    # calculate prediction sfor output
    def predictions(self, outputs):
        return np.argmax(outputs, axis=1)

# sigmoid activation
class Activation_Sigmoid:

    # forward pass
    def forward(self, inputs, training):
        # save input and calculate/save output of the sigmoid function
        self.input = inputs
        self.output = 1 / (1 + np.exp(-inputs))

    # backward pass
    def backward(self, dinputs):
        # derivative - calculates from output of the sigmoid function
        self.dinputs = dinputs * (1 - self.output) * self.output

    # calculate prediction sfor output
    def predictions(self, outputs):
        return (outputs > 0.5) * 1

# linear activation
class Activation_Linear:
    # forward pass
    def forward(self, inputs, training):
        # just remember values
        self.input = inputs
        self.output = inputs
    #backward pass
    def backward(self, dinputs):
        # 1 is derivative, 1 * dvalues = dvalues - chain rule
        self.dinputs = dinputs.copy()

    # calculate prediction sfor output
    def predictions(self, outputs):
        return outputs

##########################   losses   ##########################
# common loss class
class Loss:
    
    def remember_trainable_layers(self, trainable_layers):
        self.trainable_layers = trainable_layers

    # calculates the data and regularisation losses
    # given model output and ground truth values
    def calculate(self, output, y, *, include_regularization=False):
        # calculate sample losses
        sample_losses = self.forward(output, y)
        # calc mean losses
        data_loss = np.mean(sample_losses)
        # add accumulated sum of losses and sample count
        self.accumulated_sum += np.sum(sample_losses)
        self.accumulated_count += len(sample_losses)
        # if just data loss - return it
        if not include_regularization:
            return data_loss
        # return the data and regularization losses
        return data_loss, self.regularization_loss()
    
    def calculate_accumulated(self, *, include_regularization=False):
        # calculate mean loss
        data_loss = self.accumulated_sum / self.accumulated_count
        # if just data loss - return it
        if not include_regularization:
            return data_loss
        # return the data and regularization losses
        return data_loss, self.regularization_loss()

    def new_pass(self):
        self.accumulated_sum = 0
        self.accumulated_count = 0

    # for model object
    def regularization_loss(self):

        # 0 by default
        regularization_loss = 0

        # calculate regularization loss
        # iterate all iterable layers
        for layer in self.trainable_layers:
            # L1 regularization
            # calculate only when fator greater then 0
            if layer.weight_regularizer_l1 > 0:
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
    def backward(self, dinputs, y_true):
        samples = dinputs.shape[0]
        dinputs = dinputs.copy()  # copy so we can safely modify
        dinputs[range(samples), y_true] -= 1
        dinputs = dinputs / samples
        self.dinputs = dinputs

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
    def backward(self, dinputs, y_true):
        # clip data to prevent division by 0
        # clip both sides to not drag mean towards any value
        clipped_dinputs = np.clip(dinputs, 1e-7, 1 - 1e-7)

        # gradient on values
        self.dinputs = -(y_true / clipped_dinputs - (1 - y_true) / (1 - clipped_dinputs))
        #self.dinputs = -(y_true / dinputs - (1 - y_true) / (1 - dinputs))

# mean squared error loss
class Loss_MeanSquaredError(Loss):  #L2 loss

    # forward pass
    def forward(self, y_pred, y_true):
        #calculate loss
        data_loss = 2 * np.mean((y_true - y_pred)**2, axis=-1)
        # retrn losses
        return data_loss

    # backward pass
    def backward(self, dinputs, y_true):
        # gradient on values
        self.dinputs = -2 * (y_true - dinputs)# or -2 ?

# mean absolute error
class Loss_meanAbsoluteError(Loss):  #L1 loss

    # forward pass
    def forward(self, y_pred, y_true):
        # calculate loss
        data_loss = np.mean(np.abs(y_true - y_pred), axis=-1)
        # return losses
        return data_loss

    # backward pass
    def backward(self, dinputs, y_true):
        # gradient on values
        self.dinputs = - np.sign(y_true - dinputs)


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


# model class
class Model:

    def __init__(self):
        # create a list of network objects
        self.layers = []
        # softmax classifier's output object
        self.softmax_classifier_output = None

    def add(self, layer):
        self.layers.append(layer)
    
    def set(self, *, loss, optimizer, accuracy):
        self.loss = loss
        self.optimizer = optimizer
        self.accuracy = accuracy

    def train(self, X, y, *, epochs=1, batch_size=None, print_every=1, validation_data=None):
        # initialize accuracy object
        self.accuracy.init(y)
        # default value i batch size is not being set
        train_steps = 1
        # if there is validation data passed set default number of steps
        # for validation as well
        if validation_data is not None:
            validation_steps = 1
            # for better readability
            X_val, y_val = validation_data
        # calculate number of steps
        if batch_size is not None:
            train_steps = len(X) // batch_size
            # dividing rounds down. if there are some remaining data,
            # but not full batch, this won't include it
            # add 1 to include this not full batch
            if train_steps * batch_size < len(X):
                train_steps += 1
            if validation_data is not None:
                validation_steps = len(X_val) // batch_size
                if validation_steps * batch_size < len(X):
                    validation_steps += 1
        # main training loop
        for epoch in range(1, epochs+1):
            print(f'epoch: {epoch}')
            # reset accumulated values in loss and accuracy objects
            self.loss.new_pass()
            self.accuracy.new_pass()
            
            # iterate over steps
            for step in range(train_steps):
                # if batch size is not set -
                # train using one step and full dataset
                if batch_size is None:
                    batch_X = X
                    batch_y = y
                # oterwise slice a batch
                else:
                    batch_X = X[step*batch_size:(step+1)*batch_size]
                    batch_y = y[step*batch_size:(step+1)*batch_size]
                # perform the fwd pass
                output = self.forward(batch_X, training=True)
                # calculate loss
                data_loss, regularization_loss = self.loss.calculate(output, batch_y, include_regularization=True)
                loss = data_loss + regularization_loss
                # get predictions and calculate an accuracy
                predictions = self.output_layer_activation.predictions(output)
                accuracy = self.accuracy.calculate(predictions, batch_y)
                # backwd pass
                self.backward(output, batch_y)
                # optimize (update parameters)
                self.optimizer.pre_update_params()
                for layer in self.trainable_layers:
                    self.optimizer.update_params(layer)
                self.optimizer.post_update_params()
                # print a summary
                if not step % print_every:
                    print(f'step: {step}, ' + f'acc: {accuracy:.3f}, ' + f'loss: {loss:.3f} (' + f'data_loss: {data_loss:.3f}, ' + f'reg_loss: {regularization_loss:.3f}), ' + f'lr: {self.optimizer.current_learning_rate}')
            # get and print epoch loss and acuracy
            epoch_data_loss, epoch_regularization_loss = self.loss.calculate_accumulated(include_regularization=True)
            epoch_loss = epoch_data_loss + epoch_regularization_loss
            epoch_accuracy = self.accuracy.calculate_accumulated()
            print(f'training, ' + f'acc: {epoch_accuracy:.3f}, ' + f'loss: {epoch_loss:.3f} (' + f'data_loss: {epoch_data_loss:.3f}, ' + f'reg_loss: {epoch_regularization_loss:.3f}, ' + f'lr: {self.optimizer.current_learning_rate}')
            # if there is validation data
            if validation_data is not None:
                # reset accum vals in loss and acc object
                self.loss.new_pass()
                self.accuracy.new_pass()
                # iterate over steps
                for step in range(validation_steps):
                    if batch_size is None:
                        batch_X = X_val
                        batch_y = y_val
                    # oterwise slice a batch
                    else:
                        batch_X = X_val[step*batch_size:(step+1)*batch_size]
                        batch_y = y_val[step*batch_size:(step+1)*batch_size]
                    # perform the forward pass
                    output = self.forward(batch_X, training=False)
                    # calulate the loss
                    loss = self.loss.calculate(output, batch_y)
                    # get predictions and calulate an accuracy
                    predictions = self.output_layer_activation.predictions(output)
                    accuracy = self.accuracy.calculate(predictions, batch_y)
                    # get and print validation loss and acc
                    validation_loss = self.loss.calculate_accumulated()
                    validation_accuracy = self.accuracy.calculate_accumulated()
                    # print a summary
                    print (f'validation, ' + f'acc: {validation_accuracy:.3f}, ' + f'loss: {validation_loss:.3f}')

    def forward(self, X, training):

        # call forward method on the input layer
        # this will set the output property that
        # the first layer in "prev" object is expecting
        self.input_layer.forward(X, training)
        # call fwd method of every object in a chain
        # pas  output of th previous object as a parameter
        for layer in self.layers:
            layer.forward(layer.prev.output, training)
        # "layer" is now the last object from the list,
        # return it's output
        return layer.output

    def backward(self, output, y):
        # if softmax classifier
        if self.softmax_classifier_output is not None:       
            # first call backward method
            # on the combined activation/loss
            # this will set dinputs property that the last
        # layer will try to access shortly
            self.softmax_classifier_output.backward(output, y)
            # sine we'll not call backward method of the last layer
            # which is Softmax activation
            # as we used combined activation/loss object, let's set dinputs(dvalues) in this object
            self.layers[-1].dinputs = self.softmax_classifier_output.dinputs
            # calling backward method going though all the objects but last
            # in reversed order passing dinputs(dvalues) as a parameter
            for layer in reversed(self.layers[:-1]):
                layer.backward(layer.next.dinputs)
        #self.loss.backward(output, y)
            return
        # first call backward method on the loss
        # this will set dinputs(dvalues) property that the last
        # layer will try to access shortly
        self.loss.backward(output, y)
        # calling backward method going though all the objects
        # in reversed order passing dinputs(dvalues) as a parameter
        for layer in reversed(self.layers):
            layer.backward(layer.next.dinputs)
    
    def finalize(self):

        # create and set the input layer
        self.input_layer = Layer_Input()

        # count all the objects
        layer_count = len(self.layers)
        
        # init a list containing trainable layers:
        self.trainable_layers = []

        # iterate the objects
        for i in range(layer_count):
            # if it's the first one,
            # the previous called object will e the input layer
            if i == 0:
                self.layers[i].prev = self.input_layer
                self.layers[i].next = self.layers[i+1]

            # all layers exept for the first and the last
            elif i < layer_count - 1:
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.layers[i+1]

            # the last layer - the next object is loss
            else:
                self.layers[i].prev = self.layers[i-1]
                self.layers[i].next = self.loss
                self.output_layer_activation = self.layers[i]


            # if layer contains an attribute called "weights",
            # it's a trainable layer.
            # add it to the list of trainable layers
            # we don't need to check for biases
            if hasattr(self.layers[i], 'weights'):
                self.trainable_layers.append(self.layers[i])

            # update loss objects with trainable layers
            self.loss.remember_trainable_layers(self.trainable_layers)
        
        # if output activation i Softmax and loss function is Categorical Cross-Entropy
        # create an object of combined ativation
        # and loss function containing faster gradient calculation
        if isinstance(self.layers[-1], Activation_Softmax) and isinstance(self.loss, Loss_CategoricalCrossentropy):
            # create an object of ombined activation and loss function
            self.softmax_classifier_output = Activation_Softmax_Loss_CategoricalCrossentropy()

# input layer
class Layer_Input:

    # forward pass
    def forward(self, inputs, training):
        self.output = inputs

class Accuracy:
    # calculates an accuracy
    # given predictions and ground truth values
    def calculate(self, predictions, y):
        # get comparison results
        comparisons = self.compare(predictions, y)
        # calculate an accuracy
        accuracy = np.mean(comparisons)
        # add accumulated sum of matching values and sample count
        self.accumulated_sum += np.sum(comparisons)
        self.accumulated_count += len(comparisons)
        # return accuracy
        return accuracy

    # calculates accumulated accuray
    def calculate_accumulated(self):
        # calculate an accuracy
        accuracy = self.accumulated_sum / self.accumulated_count
        return accuracy

    def new_pass(self):
        self.accumulated_sum = 0
        self.accumulated_count = 0

# accuracy calculation for regression model
class Accuracy_Regression(Accuracy):

    def __init__(self):
        # create precision property
        self.precision = None
        # calculate preision value
        # based on passed in ground truth
    def init(self, y, reinit=False):
        if self.precision is None or reinit:
            self.precision = np.std(y) / 250
    # compare predictions to the ground truth values
    def compare(self, predictions, y):
        return np.absolute(predictions - y) < self.precision

class Accuracy_Categorical(Accuracy):
    # no initialization is needed
    def init(self, y):
        pass
    # compares preditions to the ground truth values
    def compare(self, predictions, y):
        return predictions == y

class Activation_Softmax_Loss_CategoricalCrossentropy():
    # backward pass
    def backward(self, dinputs, y_true):
        # numer of samples
        samples = len(dinputs)
        # copy so we can safely modify
        self.dinputs = dinputs.copy()
        # alculate gradient
        self.dinputs[range(samples), y_true] -= 1
        # normalize gradient
        self.dinputs = self.dinputs / samples


#############################################################################################
#######################################   FUNCTIONS   #######################################
#############################################################################################

def load_mnist_dataset(dataset, path):
    # scan all the dirrectories and create a list of labels
    labels = os.listdir(os.path.join(path, dataset))
    # create lists for samples and labels
    X = []
    y = []
    # for each label folder
    for label in labels:
        # and for each image in given folder
        for file in os.listdir(os.path.join(path, dataset, label)):
            # read the image
            image = cv2.imread(os.path.join(path, dataset, label, file), cv2.IMREAD_UNCHANGED)
            # and append it and a label to the lists
            X.append(image)
            y.append(label)
    # convert the data to proper numpy arrays and return
    return np.array(X), np.array(y).astype('uint8')

# MNIST dataset (train + test)
def create_data_mnist(path):
    # load both sets separately
    X, y = load_mnist_dataset('train', path)
    X_test, y_test = load_mnist_dataset('test', path)
    # and return all the data
    return X, y, X_test, y_test



#############################################################################################
##########################################   MAIN   #########################################
#############################################################################################
# create dataset
print ('Collecting data...')
X, y, X_test, y_test = create_data_mnist('etc/data/fashion/fashion_mnist_images')

keys = np.array(range(X.shape[0]))
print ('Shuffle keys...')
np.random.shuffle(keys)
print ('Apply new order...')
X = X[keys]
y = y[keys]

# scale mnist features (from -1 to 1)
print('Scaling...')
X = (X.astype(np.float32) - 127.5) / 127.5
X_test = (X_test.astype(np.float32) - 127.5) / 127.5

# check preprocessing
# proper scale
#print(X.min(), X.max())
# check shape of input data (should be 60000, 28, 28)
#print(X.shape)

# reshape to vector (flatten)
print ('Reshape 2D into vector')
X = X.reshape(X.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

'''
# scale and reshape
X = (X.reshape(X.shape[0], -1).astype(np.loat32) - 127.5) / 127.5
X_test = (X_test.reshape(X_test.shape[0], -1).astype(np.loat32) - 127.5) / 127.5
'''

'''keys = np.array(range(X.shape[0]))
print ('Shuffle keys...')
np.random.shuffle(keys)

print ('Apply new order...')
X = X[keys]
y = y[keys]'''

# slice check
'''print(y[4])
import matplotlib.pyplot as plt
plt.imshow((X[4].reshape(28, 28)))
plt.show()'''


model = Model()

# add layers
model.add(Layer_Dense(X.shape[1],64, weight_regularizer_l2=5e-4, bias_regularizer_l2=5e-4))
model.add(Activation_ReLU())
model.add(Layer_Dropout(0.1))
model.add(Layer_Dense(64,64))
model.add(Activation_ReLU())
model.add(Layer_Dense(64,64))
model.add(Activation_ReLU())
model.add(Layer_Dense(64,10))
model.add(Activation_Softmax())

# set loss and optimizer
model.set(loss=Loss_CategoricalCrossentropy(),optimizer=Optimizer_Adam(learning_rate=0.001, decay=5e-6), accuracy=Accuracy_Categorical())

# finalize the model
model.finalize()

# train model
model.train(X, y, epochs=5, batch_size=32, print_every=100, validation_data=(X_test, y_test))


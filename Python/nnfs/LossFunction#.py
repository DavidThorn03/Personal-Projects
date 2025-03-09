import numpy as np
from nnfs.datasets import spiral_data


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


class Activation_Softmax:
    def forward(self, inputs):
        exp_values = np.exp(inputs -np.max(inputs, axis=1, keepdims=True))
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True)


# NEW STUFF
class Loss: # basic loss calculation acting as abstract class
    def calculate(self, output, y): # average the output of the loss function
        sample_losses = self.forward(output, y)
        data_loss = np.mean(sample_losses)
        return data_loss


class Loss_CategoricalCrossentropy(Loss): # loss function we are using
    def forward(self, y_pred, y_true):
        samples = len(y_pred)
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-1) # explained below

        if len(y_true.shape) == 1: # when target array is 1 dimention, where each value is where the label/correct value is for each batch is(same as 1 in one hot value)
            correct_confidence = y_pred_clipped[range(samples), y_true]
            """
            take the pre clipped values and reference them to each of the true values for each batch
            """
        elif len(y_true.shape) == 2: # when the target array is 2 dimentions of one hot encoded vectors, each value is either a 1(if its the one hot value) or 0(if its not)
            correct_confidence = np.sum(y_pred_clipped*y_true, axis=1)
            """
            same as the long version of the one hot encoded calculation below
            """

        negative_log_likelihood = -np.log(correct_confidence)
        return negative_log_likelihood

X, y= spiral_data(100, 3)

dense1 = Layer_Dense(2, 3)
activation1 = Activation_ReLU()

dense2 = Layer_Dense(3, 3)
activation2 = Activation_Softmax()

dense1.forward(X)
activation1.forward(dense1.output)

dense2.forward(activation1.output)
activation2.forward(dense2.output)

print(activation2.output[:5])

# NEW STUFF
loss_function = Loss_CategoricalCrossentropy() # create loss function
loss = loss_function.calculate(activation2.output, y) # use it to find
print(loss)

"""
Loss is a measure of how wrong we are
Needed in training to understand how we can tweak the network

Calculation to find the loss
We use categorical cross entropy to get the loss (when soft max like above is used) 
This means we only worry about how wrong the correct class, not how correct the program thinks the wrong classes are
ie, how far from 1 the output neuron that should be 1 is

this can either be done by taking only the value for the correct class(same as y_true.shape == 1 above)
here, we take the true class value(x) and perform the following operation 
-log(x)

or, it can be done with the traditional one hot encoded calculation
with [0, 1, 0] for the one hot encoded portion and [0.4, 0.1, 0.5] for the output values
the equation 
loss = -(math.log(softmax_output[0]) * target_output[0] +
         math.log(softmax_output[1]) * target_output[1] +
         math.log(softmax_output[2]) * target_output[2])

in the solution above, we have a 1 dimensional or 2 dimensional array as we need to find the average loss across all batches

Before doing this log functions we do the np.clip(y_pred, 1e-7, 1-1e-1) command
this ensure the output values are between 1e-7 and 1-1e-1
this is needed as -log0 is infinite, meaning that if true class output is 0, its loss value will be calculated as infinite,
as will the average loss
this will result in code errors and unusable results, so the above operation ensures its not

In summary, the loss function takes the output from the correct class, the -log of it
Because training is done it batches, the loss function the averages the losses of all batches to get the final loss value
"""

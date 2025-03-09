import numpy as np
from nnfs.datasets import spiral_data


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU: # only used to find hidden layers
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


# NEW SHIT STARTS HERE-----------------------------
class Activation_Softmax: # needed for final output layer
    def forward(self, inputs):
        exp_values = np.exp(inputs -np.max(inputs, axis=1, keepdims=True)) # find the greats value per batch, take it away from others and find exponent
        self.output = exp_values / np.sum(exp_values, axis=1, keepdims=True) # get each batch outputs as probability


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

"""
SOFT MAX ACTIVATION FUNCTION
Needed for final layer so we can find "how wrong we are" and probabilities of each being right according to the network

First we get the exponent of each value so that we can get accurate probabilities for negative values
Leaving equal to 0 wont let us accurately know how wrong we were
Modularising to get positives that can be added to probability completely switches their meaning(most likely is now least)
Before finding exponent we find the largest value for the batch and take away from all batch values, making exponent values between 1 and 0 and still relivant to eachother
Using exponent works without this step, but results may get so large they will break program

Then, each batch is turned to probability to see how likely each value is, using value / total value on all parts
Now the results of each batch add up to equal 1

axis=1, keepdims=True) means calculation is done separately on each batch/row of input
"""



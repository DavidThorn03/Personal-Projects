import numpy as np

np.random.seed(0)#random function

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1, 2],
     [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):#constructor for layer class taking in number of inputs/previous layer neurons and neurons
        self.weights = 0.1*np.random.randn(n_inputs, n_neurons)#creates weight matrix for layer by randomly generating numbers between -1 and 1
        self.biases = np.zeros((1, n_neurons))#creates baises for layer neurons

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases#multying matrixes for batches and weights to get layer output for all batches


layer1 = Layer_Dense(4, 5)#layer one with 5 neurons and 4 initial inputs
layer2 = Layer_Dense(5, 2)#as layer one had 5 neurons, this layer has 5 inputs, and in this case 2 neurons

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)

"""
Same logic as basic2layerbatch but done with class and randomly generated weights
NOTE: as weights matrix was made with inputs * neurons instead of neurons * inputs it doesnt need to be transposed
"""
import numpy as np
from nnfs.datasets import spiral_data

X, y = spiral_data(100, 3) # generate data


class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU: # new class for activation function
    def forward(self, inputs):
        self.output = np.maximum(0, inputs) # if input<0, output = 0, else output = input


layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()

layer1.forward(X)
activation1.forward(layer1.output)
print(activation1.output)


#to show these patterns using matplotlib
import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="brg")
plt.show()


"""
MAIN LEARNING FROM THIS PART IS ACTIVATION FUNCTION
no activation function has same result as linear activation function
Activation function(non linear) is needed as if it isnt all neurons and final output will always have
linear output only, which isnt good for more variable data with no linear values 
ie, ai to map non linear functions(exponential, logarithmic etc) will only be able to "best fit" with a line


this changes the output data before it goes to the next layer 
can use sigmoid:
    s shape between 0 and 1, not good as good as never 0 or 1
    or ReLU: 
    input < 0 output 0, else output 1, not good as no variability (on or off)

we use Activation ReLU:
    if input<0 output 0, else output 1









 method to generate input data for spiral data
 use spiral_data to generate, code for method below

 this makes X batches of 2 variables each with with y classes
 the data generated produces spiral patters on a 2 dimensional plane(2 variables),
 with each pattern having X coordinates making up that pattern
 with y spiral patterns generated for our system to map (output)

 def create_data(points, classes):#number feacher sets for number of classes
    X = np.zeros((points*classes, 2))
    y = np.zeros(points*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1.0, points)#radians
        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y
"""

import numpy as np


inputs = [[1, 2, 3, 2.5], #each vector represents one reading for each neuron
          [2.0, 5.0, -1, 2],
          [-1.5, 2.7, 3.3, -0.8]]#all combined are different readings (3), for the same neurons (4), where each set of readings are proccessed seporatly

weights = [[0.2, 0.8, -0.5, 1],#weights stay the same as no new neurons have been made
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

weights2 = [[0.1, -0.14, 0.5],#passing through 2 layers of neurons(same way any amout would be passed)
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]#each layer has its own weights and each neuron has its own biases

layer1_outputs = np.dot(inputs, np.array(weights).T) + biases#get layer one values from input
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2#and pass layer ones values to get layer two's

print(layer1_outputs)

"""
Layer concept is simple, same as inputs for first layer, using previous layers values instead of input

Batch multiplication is done using 2 matrices instead of one matrix and one vector
For this to work matrix multiplication is used
This wont initially work as matrix multiplication doesnt work with 2 matrices of the same shape
ie two 3*4 dont work as rows of the first are multiplied by colums of the second, 4 values cant be multiplied by 3
ie 1*0.2 + 2*0.5 + 3*0.8 + 2.5*? for the first row and column of layer one 
So, one matrix must be flipped (transposed)
Changing the example above to:
1*0.2 + 2*0.8 + 3*-0.5 + 2.5*1 for the first row and column of layer one
Which gives us a 3*3 input matrix for layer 2
"""

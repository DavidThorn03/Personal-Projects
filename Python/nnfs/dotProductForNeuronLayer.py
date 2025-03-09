import numpy as np


inputs = [1, 2, 3, 2.5] #input neurons values

weights = [[0.2, 0.8, -0.5, 1], #weight for output neuron 1
           [0.5, -0.91, 0.26, -0.5], #weight for output neuron 2
           [-0.26, -0.27, 0.17, 0.87]] #weight for output neuron 3

biases = [2, #bias for output neuron 1
          3, #bias for output neuron 2
          0.5] #bias for output neuron 3

outputs = np.dot(weights, inputs) + biases

print(outputs)

"""" np.dot does the same as:
Multiply each input(previous neuron layer) by their respective weights(connecting each input to each output)
in each vector and add their biases(bound to output layer neuron)

               weights relating to 
               each output layer 
               neuron connection    bias for
    inputs     all input neurons    output neuron
[1, 2, 3, 2.5]*[0.2, 0.8, -0.5, 1] + 2 = 1*0.2 + 2*0.8 + 3*-0.5 + 2.5*1 + 2 = 4.8
[1, 2, 3, 2.5]*[0.5, -0.91, 0.26, -0.5] + 3 = 1.21
[1, 2, 3, 2.5]*[-0.26, -0.27, 0.17, 0.87] + 0.5 = 2.385


done in java with:
import java.util.Arrays;

public class P003DotProduct {
  public static void main(String[] args) {
    double[] inputs = { 1.0, 2.0, 3.0, 2.5 };

    double[][] weights = {
      { 0.2, 0.8, -0.5, 1 },
      { .5, -0.91, 0.26, -0.5 },
      { -0.26, -0.27, 0.17, 0.87 }
    };

    double[] biases = { 2, 3, 0.5 };

    System.out.println(Arrays.toString(add(dotProduct(weights, inputs), biases)));
  }

  private static double[] dotProduct(double[][] input1, double[] input2) {
    double[] outputs = new double[input1.length];

    for (int i = 0; i < input1.length; i++) {
      double output = 0;
      for (int j = 0; j < input2.length; j++) {
        output += input1[i][j] * input2[j];
      }
      outputs[i] = output;
    }

    return outputs;
  }

  private static double[] add(double[] input1, double[] input2) {
    double[] output = new double[input1.length];

    for (int i = 0; i < input1.length; i++) {
      output[i] = input1[i] + input2[i];
    }

    return output;
  }
}






done in python with:
def dot_product(matrix, vector):
    outputs = [0] * len(matrix)
    for i in range(len(matrix)):
        output = 0
        for j in range(len(vector)):
            output += matrix[i][j] * vector[j]
        outputs[i] = output
    return outputs

def add(vector1, vector2):
    return [vector1[i] + vector2[i] for i in range(len(vector1))]

if __name__ == "__main__":
    inputs = [1.0, 2.0, 3.0, 2.5]

    weights = [
        [0.2, 0.8, -0.5, 1],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]
    ]

    biases = [2, 3, 0.5]

    result = add(dot_product(weights, inputs), biases)
    print(result) 
"""
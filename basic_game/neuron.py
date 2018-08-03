import math
import numpy as np

class Neuron():
    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.input_weights = np.random.randn(1, self.num_inputs)
        self.output_weights = np.random.randn(1, self.num_outputs)
        self.fitness = 0

    def sigmoid(self, x):
        return 1/(math.exp(-x)+1)

    def stimulate(self, inputs):
        hidden = np.dot(self.input_weights, inputs)
        return self.sigmoid(hidden)*self.output_weights

    def mutate(self, rate):
        self.input_weights += np.random.randn(1, self.num_inputs)*rate
        self.output_weights += np.random.randn(1, self.num_outputs)*rate

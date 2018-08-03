import numpy as np
from neuron import *
import math
import random

class NeuronPool():
    def __init__(self, num_inputs, num_outputs, population):
        self.population = population
        self.neurons = []
        self.neurons = [Neuron(num_inputs, num_outputs) for i in range(population)]

    def get_neurons(self, number):
        return random.sample(self.neurons, number)

    def get_sample_neurons(self):
        bag = []
        for neuron in neurons:
            if np.random.choice(2, p=[neuron.fitness, 1-neuron.fitness]) == 0:
                bag += [neuron]
        return bag

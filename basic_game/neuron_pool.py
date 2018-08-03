import numpy as np
from neuron import *
import math
import random
import functools
class NeuronPool():
    def __init__(self, num_inputs, num_outputs, population):
        self.population = population
        self.neurons = []
        self.neurons = [Neuron(num_inputs, num_outputs) for i in range(population)]

    def get_neurons(self, number):
        return random.sample(self.neurons, number)

    def get_sample_neurons(self):
        bag = []
        for neuron in self.neurons:
            if np.random.choice(2, p=[neuron.fitness, 1-neuron.fitness]) == 0:
                bag += [neuron]
        return bag

    def decay_fitness(self):
        for neuron in self.neurons:
            neuron.fitness = 99*neuron.fitness/100
            neuron.fitness_update = False

    def print_fitness(self):
        print([neuron.fitness for neuron in self.neurons])

    def best_neurons(self, number):
        def compare_neurons(neuron1, neuron2):
            return neuron2.fitness-neuron1.fitness
        best_neuron_list = sorted(self.neurons, key=functools.cmp_to_key(compare_neurons))
        return best_neuron_list[0:number]

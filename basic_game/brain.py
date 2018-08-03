import numpy as np
from neuron import *
import math
import random

class Brain():
    def __init__(self, neurons):
        self.neurons = neurons

    def get_move(self, raw):
        outputs = np.array([[0.,0.,0.]])
        for neuron in self.neurons:
            outputs+=neuron.stimulate(raw)
        return np.argmax(outputs)-1

    def merge(self, other_brain, number):
        return Brain(random.sample(self.neurons+other_brain.neurons, number))

    def mutate(self):
        for neuron in self.neurons:
            neuron.mutate(0.1)

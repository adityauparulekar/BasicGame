import math
import numpy as np

INPUTS = 13
HIDDEN = 5
OUTPUT = 3

class NeuralNetwork():
    def __init__(self, mutation_rate, mom=None, dad=None):
        if not mom is None:
            cross_over1 = np.random.choice(2, (HIDDEN,INPUTS), p=[0.5, 0.5])
            self.weights1 = mutation_rate*np.random.randn(HIDDEN, INPUTS) + \
                            np.multiply(cross_over1,dad.brain.weights1)+ \
                            np.multiply(1-cross_over1, mom.brain.weights1)
            cross_over2 = np.random.choice(2, (OUTPUT,HIDDEN+1), p=[0.5, 0.5])
            self.weights2 = mutation_rate*np.random.randn(OUTPUT, HIDDEN+1)+\
                            np.multiply(cross_over2, dad.brain.weights2)+\
                            np.multiply(1-cross_over2, mom.brain.weights2)
        else:
            self.weights1 = mutation_rate*np.random.randn(HIDDEN, INPUTS)
            self.weights2 = mutation_rate*np.random.randn(OUTPUT, HIDDEN+1)

    def sigmoid(self, x):
        return 1/(math.exp(-x)+1)

    def get_move(self, arena):
        hidden1 = np.transpose(np.array([[1]+[self.sigmoid(xi) for xi in np.matmul(self.weights1, arena)]]))
        return np.argmax(np.array([self.sigmoid(xi) for xi in np.matmul(self.weights2, hidden1)]))

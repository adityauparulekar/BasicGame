import math
import numpy as np
class NeuralNetwork():

    def __init__(self, mutation_rate, mom=None, dad=None):
        if not mom is None:
            cross_over1 = n.random.choice(2, (41,30), p=[0.5, 0.5])
            self.weights1 = mutation_rate*np.random.randn(41, 30)+np.multiply(cross_over1, dad)+np.multiply(1-cross_over1, mom)
            cross_over2 = n.random.choice(2, (31,10), p=[0.5, 0.5])
            self.weights2 = mutation_rate*np.random.randn(31, 10)+np.multiply(cross_over2, dad)+np.multiply(1-cross_over2, mom)
            cross_over3 = n.random.choice(2, (11,3), p=[0.5, 0.5])
            self.weights3 = mutation_rate*np.random.randn(11, 3)+np.multiply(cross_over3, dad)+np.multiply(1-cross_over3, mom)
        else:
            self.weights1 = mutation_rate*np.random.randn(41, 30)
            self.weights2 = mutation_rate*np.random.randn(31, 10)
            self.weights3 = mutation_rate*np.random.randn(11, 3)

    def sigmoid(x):
        return 1/(math.exp(-x)+1)

    def get_move(self, arena):
        hidden1 = np.array([sigmoid(xi) for xi in np.matmul(arena,self.weights1)])
        hidden2 = np.array([sigmoid(xi) for xi in np.matmul(hidden1,self.weights2)])
        return np.amax(np.array([sigmoid(xi) for xi in np.matmul(hidden2,self.weights3)]))

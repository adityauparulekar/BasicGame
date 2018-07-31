import math
import numpy as np
class NeuralNetwork():

    def __init__(self, mutation_rate, mom=None, dad=None):
        if not mom is None:
            cross_over1 = np.random.choice(2, (10,41), p=[0.5, 0.5])
            self.weights1 = mutation_rate*np.random.randn(10, 41)+np.multiply(cross_over1,dad)+np.multiply(1-cross_over1, mom)
            cross_over2 = np.random.choice(2, (10,11), p=[0.5, 0.5])
            self.weights2 = mutation_rate*np.random.randn(10, 11)+np.multiply(cross_over2, dad)+np.multiply(1-cross_over2, mom)
            cross_over3 = np.random.choice(2, (3,11), p=[0.5, 0.5])
            self.weights3 = mutation_rate*np.random.randn(3, 11)+np.multiply(cross_over3, dad)+np.multiply(1-cross_over3, mom)
        else:
            self.weights1 = mutation_rate*np.random.randn(10, 41)
            self.weights2 = mutation_rate*np.random.randn(10, 11)
            self.weights3 = mutation_rate*np.random.randn(3, 11)

    def sigmoid(self, x):
        return 1/(math.exp(-x)+1)

    def get_move(self, arena):
        hidden1 = np.transpose(np.array([[1]+[self.sigmoid(xi) for xi in np.matmul(self.weights1, arena)]]))
        #print(hidden1)
        hidden2 = np.transpose(np.array([[1]+[self.sigmoid(xi) for xi in np.matmul(self.weights2, hidden1)]]))
        #print(hidden2)
        return np.argmax(np.array([self.sigmoid(xi) for xi in np.matmul(self.weights3, hidden2)]))

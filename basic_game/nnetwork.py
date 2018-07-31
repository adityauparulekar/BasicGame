import math
import numpy as np
class NeuralNetwork():

    def __init__(self):
        self.weights1 = np.random.randn(40, 30)
        self.weights2 = np.random.randn(30, 10)
        self.weights3 = np.random.randn(10, 3)

    def sigmoid(x):
        return 1/(math.exp(-x)+1)

    def get_move(self, arena):
        hidden1 = np.array([sigmoid(xi) for xi in np.matmul(arena,self.weights1)])
        hidden2 = np.array([sigmoid(xi) for xi in np.matmul(hidden1,self.weights2)])
        return np.amax(np.array([sigmoid(xi) for xi in np.matmul(hidden2,self.weights3)]))

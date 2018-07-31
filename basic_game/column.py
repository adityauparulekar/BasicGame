import numpy as np

class Column():
    def __init__(self, parent=None):
        self.components = [0,0,0,0]
        self.parent = parent
        self.obstacle = False
        self.position = 780
        for i in range(4):
            if not parent == None:
                if not self.obstacle:
                    if self.parent.components[i] == 1:
                        self.components[i] = np.random.choice(3, p=[0.2, 0.6, 0.2])
                        if self.components[i] == 2:
                            self.obstacle = True
                    else:
                        self.components[i] = np.random.choice(3, p=[0.8, 0.1, 0.1])
                        if self.components[i] == 2:
                            self.obstacle = True
                else:
                    if self.parent.components[i] == 2:
                        self.components[i] = np.random.choice(2, p=[0.9, 0.1])
                    else:
                        self.components[i] = np.random.choice(2, p=[0.4, 0.6])
            else:
                for i in range(4):
                    if not self.obstacle:
                        self.components[i] = np.random.choice(3, p = [0.8,0.1,0.1])
                    else:
                        self.components[i] = np.random.choice(2, p=[0.9,0.1])

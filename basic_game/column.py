import numpy as np
import arcade

class Column():
    def __init__(self, num_rows, parent=None):
        self.components = [0,0,0,0]
        self.parent = parent
        self.obstacle = False
        self.position = 780
        for i in range(num_rows):
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

    def draw(self, pos):
        for i in range(4):
            if self.components[i] == 2:
                new_obstacle = arcade.Sprite("obstacle.png", OBSTACLE_SCALING)
                new_obstacle.center_x = pos
                new_obstacle.center_y = 550 - (100*i)
                self.obstacle_list.append(new_obstacle)
            elif self.components[i] == 1:
                new_coin = arcade.Sprite("coin.png", COIN_SCALING)
                new_coin.center_x = new_column.position
                new_coin.center_y = 550 - (100*i)
                self.coin_list.append(new_coin)

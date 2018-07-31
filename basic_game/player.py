import arcade
import numpy as np
from nnetwork import *

PLAYER_SCALING = 60/3016
MOVEMENT = 100

class Player(arcade.Sprite):
    def __init__(self, mom = None, dad = None):
        super().__init__("character.png", PLAYER_SCALING)
        self.center_x = 64
        self.center_y = 250
        self.mom = mom
        self.dad = dad
        self.score = 0
        self.active = 1
        self.transparent = True
        self.alpha = 0
        self.pos = 0
        if not mom is None:
            self.brain = NeuralNetwork(1)
        else:
            self.brain = NeuralNetwork(0.1, mom, dad)

    def draw(self):
        self.draw()

    def update(self, raw):
        player_move = (self.brain.get_move(raw)-1)
        if not (self.center_y + player_move > 550 or self.center_y + player_move < 250):
            self.pos += player_move
            self.center_y += player_move*MOVEMENT

import arcade
import numpy as np
from nnetwork import *

PLAYER_SCALING = 60/3016

class Player():
    def __init__(self, mom = None, dad = None):
        self.player_sprite = arcade.Sprite("character.png", PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 250
        self.player_move = 0
        self.mom = mom
        self.dad = dad
        if not mom is None:
            self.brain = NeuralNetwork(1)
        else:
            self.brain = NeuralNetwork(mom, dad, 0.1)

    def draw(self):
        self.player_sprite.draw()

    def update(self):
        if not (self.player_sprite.center_y + self.player_move > 550 or self.player_sprite.center_y + self.player_move < 250):
            self.player_sprite.center_y += self.player_move
        self.player_move = 0

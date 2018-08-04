import arcade
import numpy as np
from nnetwork import *
from neuron_pool import *
from brain import *

PLAYER_SCALING = 60/3016
MOVEMENT = 100

INPUTS = 9
OUTPUTS = 3

class Player(arcade.Sprite):
    neuron_pool = NeuronPool(INPUTS, OUTPUTS, 200)
    neuron_count = 10
    new_neurons = 3
    def __init__(self, best = False, mom = None, dad = None):
        if mom is None and best is False:
            super().__init__("character.png", PLAYER_SCALING)
            self.brain = Brain(Player.neuron_pool.get_neurons(Player.neuron_count))
            self.brain.mutate()
        elif mom is None and best is True:
            super().__init__("character.png", PLAYER_SCALING*1.5)
            self.brain = Brain(Player.neuron_pool.best_neurons(10))
        else:
            super().__init__("character.png", PLAYER_SCALING)
            self.brain = mom.brain.merge(dad.brain,Player.neuron_count-Player.new_neurons)
            self.brain.neurons += Player.neuron_pool.get_sample_neurons()
            self.brain.mutate()

        self.center_x = 64
        self.center_y = 250
        self.mom = mom
        self.dad = dad
        self.score = 0
        self.active = 1
        self.pos = 0

    def draw(self):
        self.draw()

    def update(self, raw):
        player_move = self.brain.get_move(raw)
        if not (self.center_y + player_move > 550 or self.center_y + player_move < 250):
            self.pos += player_move
            self.center_y += player_move*MOVEMENT

    def update_fitness(self):
        for neuron in self.brain.neurons:
            if neuron.fitness_update == False:
                neuron.fitness = (99*neuron.fitness+1)/100
                neuron.fitness_update = True

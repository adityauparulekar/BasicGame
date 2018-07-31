import arcade

PLAYER_SCALING = 60/3016

class Player():
    def __init__(self):
        self.player_sprite = arcade.Sprite("character.png", PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 250
        self.player_move = 0
        self.player_pos = 0

    def draw(self):
        self.player_sprite.draw()

    def update(self):
        if not (self.player_sprite.center_y + self.player_move > 550 or self.player_sprite.center_y + self.player_move < 250):
            self.player_sprite.center_y += self.player_move
        self.player_move = 0

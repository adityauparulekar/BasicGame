import arcade
from column import *
from player import *
from arena import *

MOVEMENT = 100
GAME_RUNNING = 0
GAME_OVER = 1

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "basicgame")

        arcade.set_background_color(arcade.color.AMAZON)
        self.arena = None
        self.player = None
        self.current_state = GAME_RUNNING

    def setup(self):
        self.player = Player()
        self.arena = Arena()
        self.score = 0

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)


    def draw_game(self):

        self.player.draw()
        self.arena.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
        arcade.draw_line(0, 600, 800, 600, arcade.color.WOOD_BROWN, 10)
        arcade.draw_line(0, 500, 800, 500, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 400, 800, 400, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 300, 800, 300, arcade.color.WOOD_BROWN, 3)
        arcade.draw_line(0, 200, 800, 200, arcade.color.WOOD_BROWN, 10)

    def on_draw(self):
        arcade.start_render()

        if self.current_state == GAME_RUNNING:
            self.draw_game()
        else:
            self.draw_game()
            self.draw_game_over()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player.player_move += MOVEMENT
        elif key == arcade.key.DOWN:
            self.player.player_move -= MOVEMENT

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:
            self.arena.update()
            self.player.update()

            for coin in arcade.check_for_collision_with_list(self.player.player_sprite, self.arena.coin_list):
                coin.kill()
                self.score += 1

            if len(arcade.check_for_collision_with_list(self.player.player_sprite, self.arena.obstacle_list)) != 0:
                self.current_state = GAME_OVER

def main():
    game = MyGame()
    game.setup()
    game.set_update_rate(0.3)
    arcade.run()

if __name__ == "__main__":
    main()

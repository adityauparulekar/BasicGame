import arcade
from column import *
from player import *
from arena import *

MOVEMENT = 100
GAME_RUNNING = 0
GAME_OVER = 1

NUM_PLAYERS = 2

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "basicgame")

        arcade.set_background_color(arcade.color.AMAZON)
        self.arena = None
        self.player_list = arcade.SpriteList()
        self.current_state = GAME_RUNNING

    def setup(self):

        for i in range(NUM_PLAYERS):
            self.player_list.append(Player())
        self.arena = Arena()

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)


    def draw_game(self):

        self.player_list.draw()
        self.arena.draw()

        #output = f"Score: {self.score}"
        #arcade.draw_text(output, 10, 40, arcade.color.WHITE, 14)
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

    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:
            self.arena.update()
            for player in self.player_list:
                player.update(np.array(self.arena.raw))
                for coin in arcade.check_for_collision_with_list(player, self.arena.coin_list):
                    player.score += player.active

                if len(arcade.check_for_collision_with_list(player, self.arena.obstacle_list)) != 0:
                    player.active = 0

        self.current_state = GAME_OVER

        for player in self.player_list:
            print(player.score)
            if player.active == 1:
                self.current_state = GAME_RUNNING
def main():
    game = MyGame()
    game.setup()
    game.set_update_rate(0.3)
    arcade.run()

if __name__ == "__main__":
    main()

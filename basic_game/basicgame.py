import arcade
import numpy as np

COIN_SCALING = 60/200
OBSTACLE_SCALING = 60/250
PLAYER_SCALING = 60/3016
MOVEMENT = 100
COLUMN_WIDTH = 80

GAME_RUNNING = 0
GAME_OVER = 1

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "basicgame")

        arcade.set_background_color(arcade.color.AMAZON)
        self.player_sprite = None
        self.player_list = None
        self.coin_list = None
        self.obstacle_list = None
        self.player_move = 0
        self.columns = []
        self.current_state = GAME_RUNNING

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.obstacle_list = arcade.SpriteList()

        column1 = Column()
        self.columns.append(column1)
        self.score = 0
        self.player_sprite = arcade.Sprite("character.png", PLAYER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)
    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        output = "Click to restart"
        arcade.draw_text(output, 310, 300, arcade.color.WHITE, 24)
    def draw_game(self):
        self.coin_list.draw()
        self.player_list.draw()
        self.obstacle_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
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
            self.player_move = MOVEMENT
        elif key == arcade.key.DOWN:
            self.player_move = -MOVEMENT
    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:
            for coin in self.coin_list:
                coin.center_x -= COLUMN_WIDTH
            for obstacle in self.obstacle_list:
                obstacle.center_x -= COLUMN_WIDTH
            for column in self.columns:
                column.position -= COLUMN_WIDTH
            if not (self.player_sprite.center_y + self.player_move > 550 or self.player_sprite.center_y + self.player_move < 250):
                self.player_sprite.center_y += self.player_move
            self.player_move = 0
            new_column = Column(self.columns[-1])
            self.columns.append(new_column)
            for i in range(4):
                if new_column.components[i] == 2:
                    new_obstacle = arcade.Sprite("obstacle.png", OBSTACLE_SCALING)
                    new_obstacle.center_x = new_column.position
                    new_obstacle.center_y = 550 - (100*i)
                    self.obstacle_list.append(new_obstacle)
                elif new_column.components[i] == 1:
                    new_coin = arcade.Sprite("coin.png", COIN_SCALING)
                    new_coin.center_x = new_column.position
                    new_coin.center_y = 550 - (100*i)
                    self.coin_list.append(new_coin)
            for coin in arcade.check_for_collision_with_list(self.player_sprite, self.coin_list):
                coin.kill()
                self.score += 1
            for coin in self.coin_list:
                if coin.center_x < -50:
                    coin.kill()
            for obstacle in self.obstacle_list:
                if obstacle.center_x < -50:
                    obstacle.kill()
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.obstacle_list)) != 0:
                self.current_state = GAME_OVER



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
def main():
    game = MyGame()
    game.setup()
    game.set_update_rate(0.5)
    arcade.run()

if __name__ == "__main__":
    main()

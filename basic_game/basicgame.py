import arcade
from column import *
from player import *
from arena import *
import functools

MOVEMENT = 100
GAME_RUNNING = 0
GAME_OVER = 1

NUM_PLAYERS = 1000
SURVIVORS = 50
NUM_SAME = 10

NUM_COLS_TRAINED = 2

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(800, 800, "basicgame")
        arcade.set_background_color(arcade.color.AMAZON)
        self.arena = None
        self.player_list = arcade.SpriteList()
        self.current_state = GAME_RUNNING
        self.first_gen = True
        self.best_score = 0
        self.gen_number = 0

    def best_players(self):
        def compare_players(player1, player2):
            return player2.score-player1.score
        best_player_list = sorted(self.player_list, key=functools.cmp_to_key(compare_players))
        self.best_score = best_player_list[0].score
        return best_player_list[0:SURVIVORS]

    def next_gen(self):
        self.gen_number+=1
        bp = self.best_players()
        self.player_list = arcade.SpriteList()
        for i in range(len(bp)):
            for j in range(i, len(bp)):
                if i == j:
                    for i in range(NUM_SAME):
                        self.player_list.append(Player(bp[i], bp[j]))
                self.player_list.append(Player(bp[i], bp[j]))
        print(self.player_list[0].brain.weights1)

    def next_gen1(self):
        self.gen_number+=1
        bp = self.player_list
        print([x.score for x in bp])
        def compare_players(player1, player2):
            return player2.score-player1.score
        best_player_list = sorted(bp, key=functools.cmp_to_key(compare_players))
        self.best_score = best_player_list[0].score

        self.player_list = arcade.SpriteList()
        for i in range(len(bp)):
            for j in range(i, len(bp)):
                if i == j:
                    for k in range(NUM_SAME):
                        self.player_list.append(Player(bp[i], bp[j]))
                self.player_list.append(Player(bp[i], bp[j]))
        print(self.player_list[0].brain.weights1)

    def next_gen2(self):
        self.gen_number+=1
        bp = self.player_list
        print([x.score for x in bp])
        def compare_players(player1, player2):
            return player2.score-player1.score
        best_player_list = sorted(bp, key=functools.cmp_to_key(compare_players))
        self.best_score = best_player_list[0].score

        self.player_list = arcade.SpriteList()
        for i in range(len(bp)):
            for j in range(i, len(bp)):
                if i == j:
                    for k in range(NUM_SAME):
                        self.player_list.append(Player(bp[i], bp[j]))
                self.player_list.append(Player(bp[i], bp[j]))
        print(self.player_list[0].brain.weights1)

    def next_gen3(self):
        self.gen_number+=1
        bp = self.player_list
        self.player_list = arcade.SpriteList()
        for i in range(len(bp)):
            for j in range(i, len(bp)):
                if i == j:
                    for k in range(NUM_SAME):
                        self.player_list.append(Player(bp[i], bp[j]))
                self.player_list.append(Player(bp[i], bp[j]))

    def setup(self):
        if self.first_gen:
            self.first_gen = False
            for i in range(NUM_PLAYERS):
                self.player_list.append(Player())
        else:
            self.next_gen3()
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

        output = f"Score: {self.best_score} Generation: {self.gen_number}"
        arcade.draw_text(output, 10, 80, arcade.color.WHITE, 14)
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
            self.setup()
            self.current_state = GAME_RUNNING

    def update(self, delta_time):
        if self.current_state == GAME_RUNNING:
            self.arena.update()
            for player in self.player_list:
                player_pos_list = [0,0,0,0]
                player_pos_list[player.pos] = 1
                player.update(np.array([1]+self.arena.raw[4:4*NUM_COLS_TRAINED+4]+player_pos_list))
                for coin in arcade.check_for_collision_with_list(player, self.arena.coin_list):
                    player.score += player.active

                if len(arcade.check_for_collision_with_list(player, self.arena.obstacle_list)) != 0:
                    player.active = 0
                    #player.alpha = 0.5

        del_index = 0
        while(del_index < len(self.player_list)):
            while(del_index < len(self.player_list) and self.player_list[del_index].active == 0):
                self.player_list[del_index].kill()
                del_index += 1
            del_index += 1

        if len(self.player_list) <= SURVIVORS:
            self.current_state = GAME_OVER

def main():
    game = MyGame()
    game.setup()
    game.set_update_rate(0.005)
    arcade.run()

if __name__ == "__main__":
    main()

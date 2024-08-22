import random
import math

class Player:
    def __init__(self, letter):
        self.letter = letter
    
class PlayerComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        move = random.choice(game.valid_moves())
        print(f"Computer Turn: {move}")
        return move
        
class PlayerUser(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid = game.valid_moves()
        valid_choice = False
        val = None
        while not valid_choice:
            move = int(input(f"User move: "))
            try:
                if move not in valid:
                    raise ValueError
                val = move
                valid_choice = True
            except ValueError:
                print(f"Invalid move by {self.letter}, try again")

        return val

class PlayerIA(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = self.minimax(game, self.letter)['position']
        print(f"Computer Turn: {move}")
        return move
    
    def minimax(self, game, player):
        if(len(game.valid_moves()) == 9):
            move = random.choice(game.valid_moves())
            return {'position' : move}
        else:
            max_player = self.letter
            other_player = 'O' if player == 'X' else 'X'

            if game.get_winner() == other_player:
                return {
                    'position': None,
                    'score': 1 * (len(game.valid_moves()) + 1) if other_player == max_player else -1 * (len(game.valid_moves()) + 1)
                }

            elif game.valid_moves() == []:
                return {
                    'position': None,
                    'score': 0
                }
            
            if player == max_player:
                best = {
                    'position': None,
                    'score': -math.inf
                }
            else:
                best = {
                    'position': None,
                    'score': math.inf
                }

            for possible_move in game.valid_moves():
                game.do_move(player, possible_move)
                sim_score = self.minimax(game, other_player)
                game.board[game.index[possible_move][0]][game.index[possible_move][1]] = ' '
                sim_score['position'] = possible_move
                if player == max_player:

                    if sim_score['score'] > best['score']:
                        best = sim_score

                else:
                    if sim_score['score'] < best['score']:
                        best = sim_score
            return best

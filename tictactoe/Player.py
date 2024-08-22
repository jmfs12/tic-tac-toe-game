import random

# 0 (0,0) 1 (0,1) 2 (0,2)
# 3 (1,0) 4 (1,1) 5 (1,2)
# 6 (2,0) 7 (2,1) 8 (2,2)

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

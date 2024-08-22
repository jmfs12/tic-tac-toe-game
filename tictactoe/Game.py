from Player import PlayerComputer, PlayerUser, PlayerIA
import random
import time
 
class TicTacToe:

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.index = {
            1 : (0,0), 2 : (0,1), 3 : (0,2),
            4 : (1,0), 5 : (1,1), 6 : (1,2),
            7 : (2,0), 8 : (2,1), 9 : (2,2)
        }

    def print_board(self):
        for row in self.board:
            print("\t\t\t  | " + " | ".join(row) + " |")
        print()

    def print_board_example(self, letter):
        print("####################### TIC TAC TOE GAME #######################")
        print()
        board = [[str(i+1) for i in range(j*3, (j*3)+3)] for j in range(3)]
        for row in board:
            print("\t\t\t  | " + " | ".join(row) + " |")
        print(f"Your letter is {letter}")
        print(f"Computer letter is {'X' if letter == 'O' else 'O'}")

        print()

    def valid_moves(self):
        moves = []
        valid = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i,j))

        for chave, valor in self.index.items():
            if valor in moves:
                valid.append(chave)

        return valid

    def do_move(self, letter, move):
        self.board[self.index[move][0]][self.index[move][1]] = letter

    def get_winner(self):
        rows = [row[:] for row in self.board]
        columns = [[line[i] for line in self.board] for i in range(3)]
        diagonals = [[self.board[i][i] for i in range(3)], [self.board[2][0], self.board[1][1], self.board[0][2]]]

        vec = [rows, columns, diagonals]

        for part in vec:
            win, letter = verify_winner(part)
            if win:
                return letter
        return win
    
def play(game, computer, user):
    turn = random.choice([0,1])
    
    while True:

        if(turn == 1):
            val = user.get_move(game)
            game.do_move(user.letter, val)
            game.print_board()
            turn = 0
        else:
            val = computer.get_move(game)
            time.sleep(1)
            game.do_move(computer.letter, val)
            game.print_board()
            turn = 1
            
        winner = game.get_winner()
        if not winner and game.valid_moves() == []:
            print("There was a TIE!!!")
            break
        elif not winner:
            continue
        elif winner:
            print(f"The big winner is {winner}")
            print(f"CONGRATULATIONS!!!!!") if winner == user.letter else print(f"YOU LOSE!!")
            break

        
def verify_winner(vec):
    for line in vec:
        if (line[0] == 'X' or line[0] == 'O') and line[0] == line[1] and line[0] == line[2]:
            return True, line[0]
    return False, False

        

def main():

    choice = str
    while(choice != "normal" and choice != "very hard"):
        choice = input("You wanna play in NORMAL or VERY HARD? ")
        choice = choice.lower()

    
    letter = None
    while letter != 'X' and letter != 'O':
        letter = input("Choice your letter (X or O) ")

    game = TicTacToe()
    game.print_board_example(letter)
    computer = PlayerIA('X' if letter == 'O' else 'O') if choice == "very hard" else PlayerComputer(('X' if letter == 'O' else 'O'))
    user = PlayerUser(letter)

    play(game, computer, user)
    

if __name__ == '__main__':
    main()
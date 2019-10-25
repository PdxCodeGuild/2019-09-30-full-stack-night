class Player():
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return f'name: {self.name}\ntoken: {self.token}\n'


class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[' ' for column in range(3)] for row in range(3)]

    def __repr__(self):
        # output_list = []
        # for i in range(3):
        #     output_list.append('|'.join(self.board[i]))
        # return '\n'.join(output_list)
        return '\n'.join(['|'.join(self.board[i]) for i in range(3)])

    def move(self, player, x, y):
        if self.board[x][y] != ' ':
            return f'space taken.' 
        self.board[x][y] = player.token

    def is_full(self):
        return "' '" not in str(self.board)

    def calc_winner(self):
        # rows
        for row in self.board:
            if str(row).count(self.player1.token) == 3:
                return self.player1
            elif str(row).count(self.player2.token) == 3:
                return self.player2

        for i in range(3):
            # check vertical wins
            col = [self.board[j][i] for j in range(3)]
            if all(item == self.player1.token and item != ' ' for item in col):
                return self.player1
            if all(item == self.player2.token and item != ' ' for item in col):
                return self.player2


        # check diagonal wins
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != ' ':
            if self.board[0][0] == self.player1.token:
                return self.player1
            else:
                return self.player2

        if (self.board[2][0] == self.board[1][1] == self.board[0][2]) and self.board[2][0] != ' ':
            if self.board[2][0] == self.player1.token:
                return self.player1
            else:
                return self.player2

def main():
    player1 = Player('player1', 'X')
    player2 = Player('player2', 'O')
    n_moves = 0
    game = Game(player1, player2)

    while not game.is_full():
        player_up = player1 if n_moves % 2 == 0 else player2
        n_moves += 1

        player_move = input(f'{player_up.name} enter your move (x-coordinate, y-coordinate): ')
        if player_move == 'q': break

        game.move(player_up, int(player_move.split(',')[0]), int(player_move.split(',')[1]))
        print(game)

        winner = game.calc_winner()
        if winner:
            print(f'congratulations {winner.name} ({winner.token}), you won!')
            break


main()
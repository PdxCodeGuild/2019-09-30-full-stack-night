import random

def main():
    valid_moves = ['rock', 'paper', 'scissors']
    winning_cases = [
                        ('rock', 'scissors'), 
                        ('paper', 'rock'), 
                        ('scissors', 'paper')
                    ]
    
    while True:
        user_move = input('choose your weapon (q to quit): ').lower()
        if user_move == 'q': break

        computer_move = random.choice(valid_moves)
        moves = (user_move, computer_move)

        if user_move not in valid_moves:
            print('invalid move\n')
        elif user_move == computer_move:
            print('tie')
        elif moves in winning_cases:
            print('user wins')
        else:
            print('user loses')

main()

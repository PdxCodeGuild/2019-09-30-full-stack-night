import random

def main():
    play_again = 'y'
    while play_again != 'n':
        number = random.randint(1, 10)
        n_guesses = 0

        while True:
            current_guess = input('enter guess (or r to start over): ').lower()
            if current_guess == 'r': break
            n_guesses += 1
            current_guess = int(current_guess)

            if current_guess == number: 
                print(f'congratulations! you won after {n_guesses} tries.')
                break

            print('too high') if current_guess > number else print('too low')
        play_again = input('play again? (y/n): ').lower()
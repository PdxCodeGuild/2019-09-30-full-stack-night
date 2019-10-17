import random

def main():
    play_again = 'y'
    while play_again != 'n':
        number = random.randint(1, 10)
        n_guesses = 0
        previous_guess = 0

        while True:
            current_guess = input('enter guess (or r to start over): ').lower()
            if current_guess == 'r': break

            current_guess = int(current_guess)


            # print(current_guess, previous_guess, number)
            print('too high') if current_guess > number else print('too low')
            n_guesses += 1
            if current_guess == number: 
                print(f'congratulations! you won after {n_guesses} tries.')
                break            
            if n_guesses == 1: 
                previous_guess = current_guess
                continue


            print(f'your last guess was {abs(previous_guess - number)} off, your current guess is {abs(current_guess - number)} off')

            previous_guess = current_guess
        play_again = input('play again? (y/n): ').lower()

main()
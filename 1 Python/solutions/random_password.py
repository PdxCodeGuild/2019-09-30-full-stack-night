import random
import string

# char_set = string.ascii_letters + string.digits + string.punctuation

def get_lowercase_letters(n_letters, password):
    for i in range(0, n_letters):
        password.append(random.choice(string.ascii_lowercase))

def get_uppercase_letters(n_letters, password):
    for i in range(0, n_letters):
        password.append(random.choice(string.ascii_uppercase))


def get_numbers(n_numbers, password):
    for i in range(0, n_numbers):
        password.append(random.choice(string.digits))


def get_specials(n_specials, password):
    for i in range(0, n_specials):
        password.append(random.choice(string.punctuation))



def main():
    password = []

    n_lowers = int(input('\nhow many lowercase? '))
    n_uppers = int(input('how many uppercase? '))
    n_numbers = int(input('how many numbers? '))
    n_specials = int(input('how many \'specials\'? '))

    get_lowercase_letters(n_lowers, password)
    get_uppercase_letters(n_uppers, password)
    get_numbers(n_numbers, password)
    get_specials(n_specials, password)

    # print(f'{"".join(password)}')
    print(f'\n{"".join(random.sample(password, k=len(password)))}\n')
    

main()
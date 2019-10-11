import random

messages = [
    'it is certain',
    'it is decidedly so',
    'without a doubt',
    'yes, definitely',
    'you may rely on it',
    'as i see it, yes',
    'most likely',
    'outlook good',
    'yes',
    'signs point to yes',
    'reply hazy, try again laster',
    'ask again later',
    'better not tell you now',
    'i think the spirits hate you....'
    '...'
    'cannot predict right now'
    'insert quarter to continue'
    'don\'t count on it'
    'no',
    'doubtful'
]

def main():
    while True:
        question = input('\nwhat would you ask of the oracle? ')
        print(f'\n{random.choice(messages)} \n')
        proceed = input('would you like to asuage more doubts? (y/n)').lower()
        if proceed == 'n': break

main()
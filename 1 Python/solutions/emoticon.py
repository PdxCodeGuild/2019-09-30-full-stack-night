import random

eyes = [
    ':',
    'X',
    '|',
    ';',
    '8',
    '=',
    'B'
]

noses = [
    '-',
    '^',
    '',
    '{'
]

mouths = [
    ')',
    '(',
    'D',
    '|',
    ']',
    'o'
]

num_emos = 0
while num_emos < 5:
    print(f'{random.choice(eyes)}{random.choice(noses)}{random.choice(mouths)}\n')
    num_emos += 1


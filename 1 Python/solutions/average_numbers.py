import functools

def main():
    numbers = []
    while True:
        user_input = input('enter a number (q to quit): ').lower()
        if user_input == 'q': break
        numbers.append(int(user_input))

    number_sum = functools.reduce(lambda a, x: a + x, numbers)

    print(number_sum / len(numbers))

main()
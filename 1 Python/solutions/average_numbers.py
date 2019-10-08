def main():
    numbers = []
    while True:
        user_input = input('enter a number (q to quit): ').lower()

        if user_input == 'q':
           break
        numbers.append(int(user_input))

    number_sum = 0
    for number in numbers:
        number_sum += number

    print(number_sum / len(numbers))

main()
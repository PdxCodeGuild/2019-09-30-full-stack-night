def convert(number):

        tens_digit = number // 10
        ones_digit = number % 10

        ones = [
            '',
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
            'ten'
        ]

        tens = [
            '',
            'ten',
            'twenty',
            'thirty',
            'forty',
            'fifty',
            'sixty',
            'seventy',
            'eighty',
            'ninety',
        ]

        teens = [
            'ten',
            'eleven',
            'twelve',
            'thirteen',
            'fourteen',
            'fifteen',
            'sixteen',
            'seventeen',
            'eightteen',
            'nineteen'
        ]

        hundreds = [
            '',
            'one hundred',
            'twenty',
            'thirty',
            'forty',
            'fifty',
            'sixty',
            'seventy',
            'eighty',
            'ninety',
        ]

        if tens_digit == 0 and ones_digit:
            num_text = ones[ones_digit]
        elif tens_digit == 1:
            num_text = teens[ones_digit]
        elif tens_digit and ones_digit == 0:
            num_text = tens[tens_digit]
        else:
            num_text = f'{tens[tens_digit]}-{ones[ones_digit]}'

        return num_text

def main(test):
    while True:
        if test == True:
            for num in range(1, 100):
                print(convert(num))
            return
        user_input = input('enter number (q to quit): ')
        if user_input == 'q': break
        print(convert(int(user_input)))

main(False)

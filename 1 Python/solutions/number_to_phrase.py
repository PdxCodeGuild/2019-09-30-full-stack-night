def main():
    for x in range(1, 100):
        # x = input('enter number (q to quit): ')
        # if x == 'q':
        #     break

        x= int(x)

        tens_digit = x // 10
        ones_digit = x % 10

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

        if tens_digit == 0 and ones_digit:
            num_text = ones[ones_digit]
        elif tens_digit == 1:
            num_text = teens[ones_digit]
        elif tens_digit and ones_digit == 0:
            num_text = tens[tens_digit]
        else:
            num_text = f'{tens[tens_digit]}-{ones[ones_digit]}'

        print(num_text)

main()


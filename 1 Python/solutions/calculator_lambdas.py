def main():
    operations = {
        '+': lambda l_operand, r_operand: l_operand + r_operand,
        '-': lambda l_operand, r_operand: l_operand - r_operand,
        '*': lambda l_operand, r_operand: l_operand * r_operand,
        '/': lambda l_operand, r_operand: l_operand / r_operand
    }

    while True:
        operator = input('enter operation (q to quit): ').lower()
        if operator == 'q':
            break
        l_operand = int(input('enter left operand: '))
        r_operand = int(input('enter right operand: '))

        print(operations[operator](l_operand, r_operand))

main()
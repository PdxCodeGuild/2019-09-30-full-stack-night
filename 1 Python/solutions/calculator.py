def addition(l_operand, r_operand):
    return l_operand + r_operand

def subtraction(l_operand, r_operand):
    return l_operand - r_operand

def multiplication(l_operand, r_operand):
    return l_operand * r_operand

def division(l_operand, r_operand):
    return l_operand / r_operand

def main():
    operations = {
        '+': addition,
        '-': subtraction,
        '*': multiplication,
        '/': division
    }

    while True:
        operator = input('enter operation (q to quit): ').lower()
        if operator == 'q':
            break
        l_operand = int(input('enter left operand: '))
        r_operand = int(input('enter right operand: '))

        print(operations[operator](l_operand, r_operand))

main()
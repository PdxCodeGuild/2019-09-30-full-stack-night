def main():
    total = int(input('enter dollar amount in pennies: '))

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    nQuarters = total // quarter
    remainder = total % quarter

    nDimes = remainder // dime
    remainder = remainder % dime

    nNickels = remainder // nickel
    remainder = remainder % nickel

    nPennies = remainder // penny

    print(f'\nyou have {.25 * nQuarters + .10 * nDimes + 0.05 * nNickels + 0.01 * nPennies}')
    print(f'you have {nQuarters} quarters, {nDimes} dimes, {nNickels} nickels, and {nPennies} pennies\n')

main()
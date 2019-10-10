def convert_units(data):
    conversion_factors = {
        'ft': 0.3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': 0.9144,
        'in': 0.0254
    }
    value, unit_from, unit_to = data
    converted_m = conversion_factors[unit_from] * value
    return round(converted_m / conversion_factors[unit_to], 2)


def main():

    user_input = input('\nenter the distance: ')
    convert_to_unit = input('\nenter units to convert to: ')

    user_input_split = user_input.split(" ")

    value = int(user_input_split[0])
    unit = user_input_split[1]

    print(f'\n{value} {unit} is {convert_units((value, unit, convert_to_unit))} {convert_to_unit}.\n')

main()
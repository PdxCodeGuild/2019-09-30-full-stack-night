# dictionary mapping units to conversion factors for meters
conversion_factors = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}

user_input = input('\nenter the distance: ')
convert_to_unit = input('\nenter units to convert to: ')

# split the user input on the space to separate the value from the unit
user_input_split = user_input.split(" ")

value = int(user_input_split[0])
unit = user_input_split[1]

# convert to meters using the unit the user entered as the key for the conversion_factor dictionary
converted_m = conversion_factors[unit] * value

# convert to the specified unit using the other unit the user entered as the key for the conversion_factor dictionary
converted_other = round(converted_m / conversion_factors[convert_to_unit], 2)

# print statement for quick verification. left in, but unnecessary for final code
# print(f'\n{value} {unit} is {converted_m} m.')

print(f'\n{value} {unit} is {converted_other} {convert_to_unit}.\n')

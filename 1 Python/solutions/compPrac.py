import string

# Practice problem: 1
def powers_of_two():
    return [2**x for x in range(0,10)]

print(powers_of_two())


# Practice problem: 2
# the output for this assignment on github is wrong:
# 0 is an even number.
def first_ten_even():
    return [x for x in range(20) if x % 2 == 0]

print(first_ten_even())


# Practice problem: 3
def key_swap(a_dict):
    return {value: key for key, value in a_dict.items()}

test_dict = {'a': 1, 'b': 2}
print(key_swap(test_dict))


# Practice problem: 4
def print_ascii():
    return {string.ascii_lowercase[i]: ord(string.ascii_lowercase[i]) for i in range(len(string.ascii_lowercase))}

print(print_ascii())
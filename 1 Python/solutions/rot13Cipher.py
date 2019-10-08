import string

def get_user_input(message):
    return input(message).lower()

def cipher_string_rotation(a_string, rotation_amount = 13):
    encoded_string = ''
    for char in a_string:
        index = string.ascii_lowercase.find(char)
        encoded_string += string.ascii_lowercase[(index + rotation_amount) % 26]
    return encoded_string

def cipher_string_rotation(a_string, rotation_amount = 13):
    encoded_string = ''
    for char in a_string:
        index = string.ascii_lowercase.find(char)
        encoded_string += string.ascii_lowercase[(index + rotation_amount) % 26]
    return encoded_string

def rotn(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n

        while index >= len(alphabet):
            index -= len(alphabet)
        output += alphabet[index]
    return output


def main():    
    while True:
        rotation = input('enter rotation (enter a \'q\' to quit): ')
        if rotation == 'q': break
        rotation = int(rotation)
        user_string = get_user_input('enter text to encode (enter a \'q\' to quit): ').lower()
        encoded_user_string = cipher_string_rotation(user_string, rotation)
        print(encoded_user_string)
        
main()


import string

def get_user_input(message):
    return input(message).lower()

def cipher_string_rotation(a_string, rotation_amount = 13):
    encoded_string = ''
    for char in a_string:
        index = string.ascii_lowercase.find(char)
        encoded_string += string.ascii_lowercase[(index + rotation_amount) % 26]
    return encoded_string

def main():    
    while True:
        rotation = input('enter rotation (q to quit): ')
        if rotation == 'q': break
        user_string = get_user_input('enter text to encode (enter a \'q\' to quit): ').lower()
        encoded_user_string = cipher_string_rotation(user_string, int(rotation))
        print(encoded_user_string)
        
main()


# import string

# def rot13(message):
#     print(message)
#     rotation_amount = 13
#     encoded_string = ''
#     for char in message:
#         if char in string.ascii_lowercase:
#             index = string.ascii_lowercase.find(char)
#             encoded_string += string.ascii_lowercase[(index + rotation_amount) % 26]
#         else:
#             encoded_string += char
#     return encoded_string

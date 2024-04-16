import random as random_libs
import string as string_libs


def number(length):
    characters = string_libs.digits
    random_string = ''.join(random_libs.choice(characters) for i in range(length))
    return random_string


def string(length):
    characters = string_libs.ascii_letters
    random_string = ''.join(random_libs.choice(characters) for i in range(length))
    return random_string

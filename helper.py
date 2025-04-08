import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_ten_random_string(wanted_length):
    return generate_random_string(wanted_length)

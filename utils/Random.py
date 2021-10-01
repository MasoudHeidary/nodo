from random import choice
from string import digits


def random_number(length: int = 6):
    number = ''.join(choice(digits) for i in range(length))
    return number

from random import randint
from math import gcd


MIN_EL_RANGE = 1
MAX_EL_FIRST_RANGE = 1000
MAX_EL_SECOND_RANGE = 10


def brain_gcd():
    '''
    Generates a question about the greatest common divisor.
    Computes its own answer. Returns the question and its own answer.
    :return: int, str
    '''
    text_quest = 'Find the greatest common divisor of given numbers.'
    num1 = randint(MIN_EL_RANGE, MAX_EL_FIRST_RANGE)
    num2 = randint(MIN_EL_RANGE, MAX_EL_SECOND_RANGE)

    answer_game = gcd(num1, num2)

    text_quest += '\n' + f'Question: {num1} {num2}'

    return answer_game, text_quest

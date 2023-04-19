from random import randint
from math import gcd


def brain_gcd():
    '''
    Generates a question about the greatest common divisor.
    Computes its own answer. Returns the question and its own answer.
    :return: inr, str
    '''
    TEXT_QUEST = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 1000)
    num2 = randint(1, 10)

    answer_game = gcd(num1, num2)

    TEXT_QUEST += '\n' + f'Question: {num1} {num2}'

    return answer_game, TEXT_QUEST

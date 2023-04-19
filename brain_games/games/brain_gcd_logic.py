from random import randint
from math import gcd


def brain_gcd():
    '''
    Calculates the greatest common multiple.
    :return: tuple from int
    '''
    TEXT_QUEST = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 1000)
    num2 = randint(1, 10)

    answer_game = gcd(num1, num2)

    print(TEXT_QUEST)
    print(f'Question: {num1} {num2}')
    answer_user = int(input('Your answer: '))

    return answer_game, answer_user

from random import randint


def alg_evklid(num1, num2):
    '''
    Implementation of the Euclid algorithm.
    :param num1: int
    :param num2: int
    :return: int
    '''
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    return num1 + num2


def brain_gcd():
    '''
    Generates a question about the greatest common divisor.
    Computes its own answer. Returns the question and its own answer.
    :return: inr, str
    '''
    TEXT_QUEST = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 1000)
    num2 = randint(1, 10)

    TEXT_QUEST += '\n' + f'Question: {num1} {num2}'

    answer_game = alg_evklid(num1, num2)

    return answer_game, TEXT_QUEST

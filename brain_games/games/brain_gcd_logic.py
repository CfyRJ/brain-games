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
    Calculates the greatest common multiple.
    :return: tuple from int
    '''
    TEXT_QUEST = 'Find the greatest common divisor of given numbers.'
    num1 = randint(1, 1000)
    num2 = randint(1, 1000)

    print(TEXT_QUEST)
    print(f'Question: {num1} {num2}')
    answer_user = int(input('Your answer: '))

    answer_game = alg_evklid(num1, num2)

    return answer_game, answer_user

from random import randint


def check_even(num):
    '''
    Checking a number for evenness.
    :param num: int
    :return: str
    '''
    res = 'no'

    if num % 2 == 0:
        res = 'yes'

    return res


def brain_even():
    '''
    It's a game. It asks if the number is even.
    Waiting for a 'yes' or 'no' answer.
    return: str
    '''
    num_quest = randint(0, 1000)
    answer_game = check_even(num_quest)

    print(f'Question: {num_quest}')
    answer_user = input('Your answer: ')

    return answer_game, answer_user

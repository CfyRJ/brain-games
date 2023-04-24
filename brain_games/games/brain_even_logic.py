from random import randint


GAME_CONDITIONS = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANGE = 0
MAX_RANGE = 1000


def is_even(num):
    '''
    Checking a number for evenness.
    :param num: int
    :return: bool
    '''

    return num % 2 == 0


def make_game_work():
    '''
    Generates an even number question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    return: str, str
    '''
    num_quest = randint(MIN_RANGE, MAX_RANGE)
    answer_game = is_even(num_quest)

    text_quest = f'{num_quest}'

    return answer_game, text_quest

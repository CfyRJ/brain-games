from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_RANGE = 0
MAX_RANGE = 1000


def is_even(num):
    '''
    Checking a number for evenness.
    :param num: int
    :return: bool
    '''

    return num % 2 == 0


def make_game_data():
    '''
    Generates an even number question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    return: str, str
    '''
    num_quest = randint(MIN_RANGE, MAX_RANGE)
    answer_game = 'yes' if is_even(num_quest) else 'no'

    question = f'{num_quest}'

    return answer_game, question

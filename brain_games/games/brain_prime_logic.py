from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. ' \
    'Otherwise answer "no".'

MIN_RANGE = 0
MAX_RANGE = 1000


def is_prime(num):
    """
    Is the number prime.
    :param num: int
    :return: bool
    """

    if num <= 1:
        return False

    denominator = 2

    while denominator <= num ** 0.5:
        if num % denominator == 0:
            return False

        denominator += 1
    else:
        return True


def make_game_data():
    """
    Generates an prime number question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    """
    quest_num = randint(MIN_RANGE, MAX_RANGE)

    answer_game = 'yes' if is_prime(quest_num) else 'no'

    question = f'{quest_num}'

    return answer_game, question

from random import randint


MIN_EL_RANGE = 2
MAX_EL_RANGE = 1000


def is_prime(num):
    '''
    Is the number prime.
    :param num: int
    :return: bool
    '''
    denominator = 2

    while denominator <= num ** 0.5:
        if num % denominator == 0:
            return False

        denominator += 1
    else:
        return True


def brain_prime():
    '''
    Generates an prime number question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    '''
    text_quest = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    quest_num = randint(MIN_EL_RANGE, MAX_EL_RANGE)

    answer_game = is_prime(quest_num)

    text_quest += '\n' + f'Question: {quest_num}'

    return answer_game, text_quest

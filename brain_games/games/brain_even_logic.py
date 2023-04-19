from random import randint


def is_even(num):
    '''
    Checking a number for evenness.
    :param num: int
    :return: bool
    '''

    return num % 2 == 0


def brain_even():
    '''
    Generates an even number question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    return: str, str
    '''
    text_quest = 'Answer "yes" if the number is even, otherwise answer "no".'
    num_quest = randint(0, 1000)
    answer_game = is_even(num_quest)

    text_quest += '\n' + f'Question: {num_quest}'

    return answer_game, text_quest

from random import randint


MIN_COUNT = 5
MAX_COUNT = 10
MIN_RANGE = 1
MAX_RANGE = 100
MIN_STEP = 2
MAX_STEP = 17


def brain_progression():
    '''
    Generates a question about a missing progression element.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    :return: int, str
    '''
    text_quest = 'What number is missing in the progression?'
    count_el = randint(MIN_COUNT, MAX_COUNT)
    first_el = randint(MIN_RANGE, MAX_RANGE)
    step = randint(MIN_STEP, MAX_STEP)
    last_el = first_el + (count_el - 1) * step

    progression = list(range(first_el, last_el + 1, step))

    missing_el_index = randint(0, count_el - 1)

    answer_game = progression[missing_el_index]
    progression[missing_el_index] = '..'
    progression = list(map(str, progression))
    progression = ' '.join(progression)

    text_quest += '\n' + f'Question: {progression}'

    return answer_game, text_quest

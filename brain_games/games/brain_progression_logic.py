from random import randint


def brain_progression():
    '''
    Generates a question about a missing progression element.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    '''
    TEXT_QUEST = 'What number is missing in the progression?'
    count_el = randint(5, 10)
    first_el = randint(1, 100)
    step = randint(2, 17)
    last_el = first_el + (count_el - 1) * step

    progression = list(range(first_el, last_el + 1, step))

    missing_el_index = randint(0, count_el - 1)

    answer_game = progression[missing_el_index]
    progression[missing_el_index] = '..'
    progression = list(map(str, progression))
    progression = ' '.join(progression)

    TEXT_QUEST += '\n' + f'Question: {progression}'

    return answer_game, TEXT_QUEST

from random import randint


def brain_progression():
    count_el = randint(5, 10)
    first_el = randint(1, 100)
    step = randint(2, 17)
    last_el = first_el + (count_el - 1) * step

    progression = list(range(first_el, last_el + 1, step))

    missing_el_index = randint(0, count_el - 1)

    answer_game = progression[missing_el_index]
    progression[missing_el_index] = '..'

    print('What number i missing in the progression?')
    print(f'Question: {progression}')
    answer_user = int(input('Yuor answer: '))

    return answer_game, answer_user

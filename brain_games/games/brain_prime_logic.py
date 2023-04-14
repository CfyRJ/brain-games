from random import randint


def is_prime(num):
    '''
    Is the number prime.
    :param num: int
    :return: str
    '''
    denominator = 2
    res = 'yes'

    while denominator <= num ** 0.5:
        if num % denominator == 0:
            res = 'no'
            break

        denominator += 1

    return res


def brain_prime():
    TEXT_QUEST = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    quest_num = randint(2, 1000)

    answer_game = is_prime(quest_num)

    print(TEXT_QUEST)
    print(f'Question: {quest_num}')
    answer_user = input('Your answer: ')

    return (answer_game, answer_user)

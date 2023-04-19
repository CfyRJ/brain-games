from random import randint


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
    quest_num = randint(2, 1000)

    answer_game = is_prime(quest_num)

    text_quest += '\n' + f'Question: {quest_num}'

    return answer_game, text_quest

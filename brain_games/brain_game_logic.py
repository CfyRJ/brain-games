COUNT_REPEAT = 3


def ask_quest(text_quest):
    '''
    Ask question. Return answer.
    :param text_quest: str
    :return: str
    '''
    print(f'Question: {text_quest}')
    answer_user = input('Your answer: ')

    return answer_user


def is_answers(answer_game, answer_user):
    '''
    Checking the correctness of the answer.
    :param answer_game: any
    :param answer_user: any
    :return: bool
    '''

    return True if answer_user == str(answer_game) else False


def start_game(module_game):
    '''
    Starts the game.
    :param game: module
    :return: bool
    '''


    for i in range(COUNT_REPEAT):
        answer_game, text_quest = module_game.make_game_work()

        print(module_game.GAME_CONDITION)
        answer_user = ask_quest(text_quest)

        if type(answer_game) == bool:
            answer_game = 'yes' if answer_game else 'no'

        if is_answers(answer_game, answer_user):
            print('Correct!')
            continue
        else:
            print(f"'{answer_user}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            return False
    else:
        return True


def end_game(win_lose, name):
    '''
    Says win or lose.
    :param win_lose: bool
    :param name: str
    :return: None
    '''
    if win_lose:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")

    return None

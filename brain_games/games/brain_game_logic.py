def ask_quest(text_quest):
    '''
    Ask question. Return answer.
    :param text_quest: str
    :return: str
    '''
    print(text_quest)
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


def brain_game(game):
    '''
    Starts the game.
    :param game: function
    :return: bool
    '''

    count_repeat = 3

    for i in range(count_repeat):
        answer_game, text_quest = game()
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

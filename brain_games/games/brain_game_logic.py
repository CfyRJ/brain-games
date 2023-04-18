def is_answers(answer_game, answer_user):
    '''
    Checking the correctness of the answer.
    :param answer_game: any
    :param answer_user: any
    :return: bool
    '''

    return True if str(answer_user) == str(answer_game) else False


def brain_game(game):
    '''
    Starts the game.
    :param game: function
    :return: bool
    '''

    count_repeat = 3

    for i in range(count_repeat):
        answer_game, answer_user = game()

        if is_answers(answer_game, answer_user):
            print('Correct!')
            continue
        else:
            print(f"'{answer_user}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            return False
    else:
        return True

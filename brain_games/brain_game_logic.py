import prompt


COUNT_REPEAT = 3


def play_game(module_game):
    """
    Play the game.
    :param module_game: module
    :return: None
    """

    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    for i in range(COUNT_REPEAT):
        answer_game, question = module_game.make_game_data()

        print(module_game.GAME_CONDITION)

        print(f'Question: {question}')
        answer_user = input('Your answer: ')

        if answer_user == answer_game:
            print('Correct!')
            continue
        else:
            print(f"'{answer_user}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{answer_game}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

    return None

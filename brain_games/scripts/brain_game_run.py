#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.brain_even_logic import brain_even


def check_game(str):
    '''
    Returns a function by its name.
    :param str: name game (string)
    :return: function of game
    '''

    game_dict = {
                 'brain-even':brain_even}

    if not str:
        str = input('What run game? ')

    return game_dict[str]


def check_answers(answer_game, answer_user):
    '''
    Checking the correctness of the answer.
    :param answer_game: str
    :param answer_user: str
    :return: bool
    '''
    res = False

    if answer_user == answer_game:
        res = True

    return res


def scripts_game(count_repet, game):
    '''
    Starts the game.
    :param count_repet: int
    :return: bool
    '''
    res = True
    func = check_game(game)

    for i in range(count_repet):
        answer_game, answer_user = func()

        if check_answers(answer_game, answer_user):
            print('Correct!')
            continue
        else:
            print(f"'{answer_game}' is wrong answer ;(. Correct answer was '{answer_user}'.")
            res = False
            break

    return res


def main(game = None):
    '''
    Game scenario.
    :param game: An optional parameter is the name of the game.
    :return: None
    '''
    welcome_text = 'Welcome to the Brain Games!'
    count_repet = 3
    is_continue = 'yes'

    print(welcome_text)
    name = welcome_user()

    while is_continue == 'yes':

        if scripts_game(count_repet, game):
            print(f"Congratulations, {name}!")
        else:
            print(f"Let's try again, {name}!")

        is_continue = 'no' #'no' for check hexle,  input('Want are you continue (yes/no)? ') work standart

#    print(f'Thanks for playing {name}.') # no, for check hexlet

    return None


if __name__ == '__main__':
    main()

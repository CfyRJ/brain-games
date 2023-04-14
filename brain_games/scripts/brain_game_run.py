#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.brain_even_logic import brain_even
from brain_games.games.brain_calc_logic import brain_calc
from brain_games.games.brain_gcd_logic import brain_gcd
from brain_games.games.brain_progression_logic import brain_progression
from brain_games.games.brain_prime_logic import brain_prime


def check_game(str):
    '''
    Returns a function by its name.
    :param str: name game (string)
    :return: function of game
    '''

    game_dict = {
        'brain-even': brain_even,
        'brain-calc': brain_calc,
        'brain-gcd': brain_gcd,
        'brain-progression': brain_progression,
        'brain-prime': brain_prime
    }

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
    LOSE_TEXT = 'is wrong answer ;(. Correct answer was'
    res = True
    func = check_game(game)

    for i in range(count_repet):
        answer_game, answer_user = func()

        if check_answers(answer_game, answer_user):
            print('Correct!')
            continue
        else:
            print(f"'{answer_user}' {LOSE_TEXT} '{answer_game}'.")
            res = False
            break

    return res


def main(game=None):
    '''
    Game scenario.
    :param game: An optional parameter is the name of the game.
    :return: None
    '''
    WELCOME_TEXT = 'Welcome to the Brain Games!'
    COUNT_REPET = 3
    is_continue = 'yes'

    print(WELCOME_TEXT)
    name = welcome_user()

    while is_continue == 'yes':

        if scripts_game(COUNT_REPET, game):
            print(f"Congratulations, {name}!")
        else:
            print(f"Let's try again, {name}!")

        is_continue = 'no'
# 'no' for check hexlet,
# input('Want are you continue (yes/no)? ')
# work standart

#    print(f'Thanks for playing {name}.')
# no, for check hexlet

    return None


if __name__ == '__main__':
    main()

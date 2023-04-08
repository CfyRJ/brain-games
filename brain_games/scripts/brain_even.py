#!/usr/bin/env python3


from brain_games.scripts.brain_games import Welcome
from brain_games.cli import welcome_user
from random import randint


def check_correct(strr):
    '''
    Checking the correctness of the input.
    strr: string ('no' or 'yes')
    return: bool
    '''

    check_tuple = ('no', 'yes')
    flag = False

    if strr in check_tuple:
        flag = True

    return flag


def check_even(num):
    '''
    Checking a number for evenness.
    :param num: int
    :return: str
    '''
    flag = 'no'

    if num % 2 == 0:
        flag = 'yes'

    return flag


def brain_even():
    '''
    It's a game. It asks if the number is even.
    Waiting for a 'yes' or 'no' answer. (string)
    return: bool
    '''

    num_repet = 3
    res = False

    for i in range(num_repet):
        num_quest = randint(0, 1000)
        answer_game = check_even(num_quest)

        print(f'Question: {num_quest}')
        answer_user = input(f'Your answer: ')

        if check_correct(answer_user) and answer_user == answer_game:
            print('Correct!')
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer_game}'.")
            break
    else:
        res = True

    return res


def start_game(name):
    '''
    Text about the beginning of the game.
    Game launch.
    Text about the end of the game.
    :return: None
    '''

    print('Answer "yes" if the number is even, otherwise answer "no".')

    if brain_even():
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!")

    return None


def main():
    Welcome()
    name = welcome_user()
    start_game(name)


if __name__ == '__main__':
    main()

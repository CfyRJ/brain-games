#!/usr/bin/env python3


from brain_games.scripts.brain_games import welcome
from brain_games.cli import ask_name_user
from brain_games.games.brain_game_logic import brain_game
from brain_games.games.brain_game_logic import end_game
from brain_games.games.brain_even_logic import brain_even


def main():
    welcome()
    name = ask_name_user()

    win_lose = brain_game(brain_even)

    end_game(win_lose, name)


if __name__ == '__main__':
    main()

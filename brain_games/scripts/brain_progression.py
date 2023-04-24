#!/usr/bin/env python3


from brain_games.scripts.brain_games import welcome
from brain_games.cli import ask_name_user
from brain_games.games.brain_game_logic import start_game
from brain_games.games.brain_game_logic import end_game
from brain_games.games import brain_progression_logic


def main():
    welcome()
    name = ask_name_user()

    win_lose = start_game(brain_progression_logic)

    end_game(win_lose, name)


if __name__ == '__main__':
    main()

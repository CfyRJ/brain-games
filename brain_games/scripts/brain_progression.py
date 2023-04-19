#!/usr/bin/env python3


from brain_games.scripts.brain_games import Welcome
from brain_games.cli import welcome_user
from brain_games.games.brain_game_logic import brain_game
from brain_games.games.brain_game_logic import end_game
from brain_games.games.brain_progression_logic import brain_progression


def main():
    Welcome()
    name = welcome_user()

    win_lose = brain_game(brain_progression)

    end_game(win_lose, name)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3


from brain_games.brain_game_logic import play_game
from brain_games.games import brain_gcd_logic


def main():
    play_game(brain_gcd_logic)


if __name__ == '__main__':
    main()

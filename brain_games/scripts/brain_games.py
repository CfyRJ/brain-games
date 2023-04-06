#!/usr/bin/env python3


from brain_games.cli import welcome_user


def Welcome():
    print('Welcome to the Brain Games!')


def main():
    Welcome()
    welcome_user()


if __name__ == '__main__':
    main()

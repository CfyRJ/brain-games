import prompt


def ask_name_user():
    """
    Requests and returns the username.
    :return: str
    """

    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    return name

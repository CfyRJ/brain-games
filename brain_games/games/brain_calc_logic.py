import operator
from random import randint, choice


def program_evaluation(num1, num2, oper):
    '''
    Returns the result of an expression.
    :param num1: int
    :param num2:int
    :param oper: The function to be called.
    :return: str
    '''
    operation_dict = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    return str(operation_dict[oper](num1, num2))


def brain_calc():
    '''
    Returns the game's response and the user's response.
    :return: str
    '''
    list_operations = ['+', '-', '*', '/']

    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operation = choice(list_operations)

    answer_game = program_evaluation(num1, num2, operation)

    print(f'Question: {num1} {operation} {num2}')
    answer_user = input('Your answer: ')

    return (answer_game, answer_user)

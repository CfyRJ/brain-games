import operator
from random import randint, choice


GAME_CONDITION = 'What is the result of the expression?'

MIN_RANGE = 0
MAX_RANGE1 = 1000
MAX_RANGE2 = 10


def calculate_expression(num1, num2, operation):
    """
    Returns the result of an expression.
    :param num1: int
    :param num2: -
    :param operation: The function to be called.
    :return: str
    """
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    return str(operations[operation](num1, num2))


def make_game_data():
    """
    Generates an expression question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    :return: str
    """
    operations = ['+', '-', '*']

    num1 = randint(MIN_RANGE, MAX_RANGE1)
    num2 = randint(MIN_RANGE, MAX_RANGE2)
    operation = choice(operations)

    answer_game = calculate_expression(num1, num2, operation)

    question = f'{num1} {operation} {num2}'

    return answer_game, question

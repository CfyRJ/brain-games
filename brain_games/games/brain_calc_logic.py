import operator
from random import randint, choice


MIN_RANGE = 0
MAX_RANGE1 = 1000
MAX_RANGE2 = 10


def calculate_expression(num1, num2, oper):
    '''
    Returns the result of an expression.
    :param num1: int
    :param num2:int
    :param oper: The function to be called.
    :return: str
    '''
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }

    return str(operations[oper](num1, num2))


def brain_calc():
    '''
    Generates an expression question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    :return: str
    '''
    text_quest = 'What is the result of the expression?'
    operations = ['+', '-', '*']

    num1 = randint(MIN_RANGE, MAX_RANGE1)
    num2 = randint(MIN_RANGE, MAX_RANGE2)
    operation = choice(operations)

    answer_game = calculate_expression(num1, num2, operation)

    text_quest += '\n' + f'Question: {num1} {operation} {num2}'

    return answer_game, text_quest

import operator
from random import randint, choice


MIN_EL_RANGE = 0
MAX_EL_FIRST_RANGE = 1000
MAX_EL_SEC_RANGE = 10


def calculate_expression(num1, num2, oper):
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
    Generates an expression question.
    Calculates the answer for an expression.
    Returns the question and its own answer.
    :return: str
    '''
    text_quest = 'What is the result of the expression?'
    list_operations = ['+', '-', '*']

    num1 = randint(MIN_EL_RANGE, MAX_EL_FIRST_RANGE)
    num2 = randint(MIN_EL_RANGE, MAX_EL_SEC_RANGE)
    operation = choice(list_operations)

    answer_game = calculate_expression(num1, num2, operation)

    text_quest += '\n' + f'Question: {num1} {operation} {num2}'

    return answer_game, text_quest

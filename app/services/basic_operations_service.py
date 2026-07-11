"""
basic_operations_service.py

Purpose
-------
Contains business logic for basic mathematical operations.
"""


class BasicOperationsService:

    @staticmethod
    def add(number1, number2):

        return number1 + number2


    @staticmethod
    def subtract(number1, number2):

        return number1 - number2


    @staticmethod
    def multiply(number1, number2):

        return number1 * number2


    @staticmethod
    def divide(number1, number2):

        if number2 == 0:

            raise ZeroDivisionError(
                "Cannot divide by zero."
            )

        return number1 / number2


# Notice that Division includes divide-by-zero validation.
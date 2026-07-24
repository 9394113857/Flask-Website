"""
number_properties_service.py

Purpose:
--------
Provide business logic for Number Properties operations.

Responsibilities:
-----------------
1. Perform mathematical property checks.
2. Return results to the controller.
3. Keep all business logic separate from Flask.

Supported Operations:
---------------------
- Even Number
- Odd Number
- Prime Number
- Composite Number
- Palindrome Number
- Armstrong Number
- Perfect Number
- Strong Number
- Happy Number
- Automorphic Number
"""


class NumberPropertiesService:
    """
    Service class for Number Properties.
    """

    @staticmethod
    def check_property(number: int, operation: str):
        """
        Dispatch the requested operation.
        """

        operations = {
            "even": NumberPropertiesService.is_even,
            "odd": NumberPropertiesService.is_odd,
            "prime": NumberPropertiesService.is_prime,
            "composite": NumberPropertiesService.is_composite,
            "palindrome": NumberPropertiesService.is_palindrome,
            "armstrong": NumberPropertiesService.is_armstrong,
            "perfect": NumberPropertiesService.is_perfect,
            "strong": NumberPropertiesService.is_strong,
            "happy": NumberPropertiesService.is_happy,
            "automorphic": NumberPropertiesService.is_automorphic,
        }

        if operation not in operations:
            return {
                "success": False,
                "message": "Invalid operation selected."
            }

        return operations[operation](number)

    @staticmethod
    def is_even(number: int):
        """
        Check whether the given number is even.
        """

        is_even = number % 2 == 0

        return {
            "success": True,
            "operation": "Even Number",
            "number": number,
            "result": is_even,
            "message": (
                f"{number} is an Even Number."
                if is_even
                else f"{number} is not an Even Number."
            ),
        }

    @staticmethod
    def is_odd(number: int):
        """
        Check whether the given number is odd.
        """

        is_odd = number % 2 != 0

        return {
            "success": True,
            "operation": "Odd Number",
            "number": number,
            "result": is_odd,
            "message": (
                f"{number} is an Odd Number."
                if is_odd
                else f"{number} is not an Odd Number."
            ),
        }

    @staticmethod
    def is_prime(number: int):
        pass

    @staticmethod
    def is_composite(number: int):
        pass

    @staticmethod
    def is_palindrome(number: int):
        pass

    @staticmethod
    def is_armstrong(number: int):
        pass

    @staticmethod
    def is_perfect(number: int):
        pass

    @staticmethod
    def is_strong(number: int):
        pass

    @staticmethod
    def is_happy(number: int):
        pass

    @staticmethod
    def is_automorphic(number: int):
        pass
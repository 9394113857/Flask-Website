"""
math_toolkit_controller.py

Purpose
-------
Handles requests for the Math Toolkit page.
"""

from flask import Blueprint
from flask import render_template
from flask import request

from app.services.math_toolkit_service import MathToolkitService
from app.services.basic_operations_service import BasicOperationsService


math_toolkit_bp = Blueprint(
    "math_toolkit",
    __name__
)


@math_toolkit_bp.route(
    "/math-toolkit",
    methods=["GET", "POST"]
)
def math_toolkit():

    page_data = MathToolkitService.get_page_data()

    result = None

    error = None

    number1 = ""

    number2 = ""

    if request.method == "POST":

        try:

            number1 = float(
                request.form["number1"]
            )

            number2 = float(
                request.form["number2"]
            )

            result = BasicOperationsService.add(
                number1,
                number2
            )

        except ValueError:

            error = "Please enter valid numbers."

        except Exception:

            error = "Something went wrong."

    return render_template(
        "math_toolkit.html",
        page_data=page_data,
        result=result,
        error=error,
        number1=number1,
        number2=number2
    )
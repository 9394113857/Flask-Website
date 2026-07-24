"""
number_properties_controller.py

Purpose:
--------
Handle requests for the Number Properties module.

Responsibilities:
-----------------
1. Display the Number Properties page.
2. Accept user input.
3. Validate basic input.
4. Call the service layer.
5. Render the result.

Note:
-----
This controller should NOT contain any mathematical logic.
All business logic belongs in the service layer.
"""

from flask import Blueprint, render_template, request

# Service (to be implemented in the next step)
from app.services.number_properties_service import NumberPropertiesService


# Blueprint
number_properties_bp = Blueprint(
    "number_properties",
    __name__,
)


@number_properties_bp.route(
    "/math-toolkit/number-properties",
    methods=["GET", "POST"],
)
def number_properties():
    """
    Display and process Number Properties.
    """

    # Default values
    number = ""
    operation = ""
    result = None
    message = ""
    error = ""

    if request.method == "POST":

        number = request.form.get("number", "").strip()
        operation = request.form.get("operation", "").strip()

        # Basic Validation
        if not number:
            error = "Please enter a number."

        else:
            try:
                number = int(number)

                # Call Service
                result = NumberPropertiesService.check_property(
                    number=number,
                    operation=operation,
                )

                message = "Operation completed successfully."

            except ValueError:
                error = "Please enter a valid integer."

    return render_template(
        "math_toolkit/_numbers.html",
        number=number,
        operation=operation,
        result=result,
        message=message,
        error=error,
    )
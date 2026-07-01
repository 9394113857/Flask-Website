"""
run.py

Purpose:
--------
Application Entry Point.

Responsibilities:
-----------------
1. Create the Flask application.
2. Start the development server.
"""

from click import echo

from app import create_app

# Create the Flask application
app = create_app()


# Start the application
if __name__ == "__main__":
    app.run(host="0.0.0.0")

# Run the application on all available network interfaces even on servers.
# This is useful for testing the application on different devices in the same network.

# venv\Scripts\activate

# Verify:
# echo $env:FLASK_APP

# Set the FLASK_APP environment variable
# Windows PowerShell:
# $env:FLASK_APP="run.py"

# Verify:
# echo $env:FLASK_APP

# Remove the environment variable from the current session
# Remove-Item Env:FLASK_APP

# Check the current value of the FLASK_APP environment variable
# echo $env:FLASK_APP

# Show all registered routes:
# flask routes


# Run Flask application
# flask run --host=0.0.0.0 --port=5001


#######################################################################################
# 1. This command with debug mode will automatically reload the server
# 2. when you make changes to the code,
# 3. which is very convenient during development.
# 4. However, remember to disable debug mode in production for security reasons.
#
# flask run --host=0.0.0.0 --port=5001 --debug 
#######################################################################################

# Note: If you have set the environment variables FLASK_RUN_HOST and
# FLASK_RUN_PORT, you can simply run:
#
# flask run --port 5001
#
# This will only work if you have set:
# FLASK_RUN_HOST=0.0.0.0
# FLASK_RUN_PORT=5001
# in your environment variables.

###################################################
# Start Flask Application ✅✅

# $env:FLASK_APP="run.py"

# flask run --host=0.0.0.0 --port=5001 --debug
# This will auto-reload the server on code changes.
###################################################





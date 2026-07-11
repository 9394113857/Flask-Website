import json

from flask import Flask, jsonify, request

from app.config import Config

from app.controllers.home_controller import home_bp
from app.controllers.calculator_controller import calculator_bp
from app.controllers.bmi_controller import bmi_bp
from app.controllers.flames_controller import flames_bp
from app.controllers.guess_controller import guess_bp
from app.controllers.about_controller import about_bp
from app.controllers.contact_controller import contact_bp
from app.controllers.math_toolkit_controller import math_toolkit_bp


def get_build_info():
    """
    Reads build metadata generated during the CI pipeline.

    During local development, build_info.json will not exist,
    so fallback values are returned.
    """
    try:
        with open("build_info.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return {
            "version": "unknown",
            "commit": "unknown",
            "branch": "unknown",
            "build_time_utc": "unknown",
            "build_time_ist": "unknown",
        }


def create_app():
    """
    Application Factory Function.

    Creates and configures the Flask application.
    Registers all Blueprints.
    Returns the ready-to-use Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Register Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(calculator_bp)
    app.register_blueprint(bmi_bp)
    app.register_blueprint(flames_bp)
    app.register_blueprint(guess_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(math_toolkit_bp)

    @app.get("/health")
    def health():
        """
        Health endpoint.

        Returns HTML when opened in a browser.
        Returns JSON for API clients.
        """

        build = get_build_info()

        # Browser response
        if "text/html" in request.headers.get("Accept", ""):
            return (
                f"""
            <html>
            <head>
                <title>🚀 Flask Website Service</title>

                <style>
                    body {{
                        font-family: Arial;
                        background: #0f172a;
                        color: white;
                        text-align: center;
                        padding-top: 60px;
                    }}

                    .card {{
                        background: #1e293b;
                        padding: 30px;
                        border-radius: 12px;
                        display: inline-block;
                        box-shadow: 0 0 20px rgba(0,0,0,0.45);
                    }}

                    h1 {{
                        color: #38bdf8;
                    }}

                    .ok {{
                        color: #22c55e;
                    }}

                    .label {{
                        color: #94a3b8;
                    }}
                    
                    .back-btn {{ 
                        display: inline-block;
                        margin-top: 20px;
                        padding: 10px 22px;
                        background: #0d6efd;
                        color: white;
                        text-decoration: none;
                        border-radius: 8px;
                        font-weight: bold;
                        transition: background 0.3s ease;
                    }}

                    .back-btn:hover {{
                        background: #0b5ed7;
                        color: white;
                    }}
                </style>

            </head>

            <body>

                <div class="card">

                    <h1>🚀 Flask Website Service</h1>

                    <p class="ok">🟢 UP</p>

                    <p><span class="label">Version:</span> {build["version"]}</p>

                    <p><span class="label">Commit:</span> {build["commit"]}</p>

                    <p><span class="label">Branch:</span> {build["branch"]}</p>

                    <p><span class="label">UTC:</span> {build["build_time_utc"]}</p>

                    <p><span class="label">IST:</span> {build["build_time_ist"]}</p>


                    <!-- Back Button -->

                    <a
                        href="/"
                        class="back-btn">

                        ← Back to Home

                    </a>

                </div>

            </body>

            </html>
            """,
                200,
            )

        # API response
        return (
            jsonify(
                {
                    "status": "UP",
                    "service": "Flask Website",
                    "message": "Application is running",
                    "build": build,
                }
            ),
            200,
        )

    return app

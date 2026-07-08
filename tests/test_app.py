# ============================================================
# 🧪 FLASK APPLICATION TEST
#
# Checks:
#
# 1. Flask app can initialize
# 2. Root endpoint returns HTTP 200
#
# Used by GitHub Actions CI
#
# ============================================================


import pytest

from app import create_app





# ============================================================
# 🔧 CREATE TEST CLIENT
#
# Uses your existing create_app()
# No testing argument because your factory
# currently does not accept it.
#
# ============================================================


@pytest.fixture
def client():


    app = create_app()


    app.config.update(
        TESTING=True
    )


    with app.test_client() as client:

        yield client






# ============================================================
# ❤️ ROOT HEALTH TEST
#
# GET /
#
# Expected:
# HTTP 200
#
# ============================================================


def test_home_page(client):


    response = client.get("/")


    assert response.status_code == 200
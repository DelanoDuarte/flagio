import pytest
from run import app


@pytest.fixture()
def client():
    # Set the Testing configuration prior to creating the Flask application
    #flask_app = my_app.create_app()

    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        # Establish an application context
        with app.app_context():
            yield client  # this is where the testing happens!
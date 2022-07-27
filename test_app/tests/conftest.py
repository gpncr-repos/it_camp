import pytest
from fastapi.testclient import TestClient

from test_app.app import app


@pytest.fixture()
def api_client():
    return TestClient(app)

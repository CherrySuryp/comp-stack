import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture
def test_client():
    return TestClient(app)

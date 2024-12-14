from fastapi.testclient import TestClient

from app.main import app

test_client = TestClient(app)


def test_ping():
    with test_client as client:
        req = client.get("/debug/ping")
    assert req.status_code == 200

def test_ping(test_client):
    with test_client as client:
        req = client.get("/debug/ping")
    assert req.status_code == 200

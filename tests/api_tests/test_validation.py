from typing import Literal

import pytest


@pytest.mark.parametrize(
    "payload,status_code",
    [
        ({"filters": {"date_range": {"start_date": "2024-01-01", "end_date": "2023-01-01"}}}, 422),
        ({"filters": {"date_range": {"start_date": "2023-01-01", "end_date": "2024-01-01"}}}, 200),
    ],
)
def test_date_validation(payload: dict, status_code: Literal[200, 422], test_client):
    with test_client as client:
        req = client.post("/summary", json=payload)
    assert req.status_code == status_code
    if status_code == 422:
        validation_error_body = req.json()["detail"][0]
        assert validation_error_body["type"] == "value_error"
        assert validation_error_body["loc"] == ["body", "filters", "date_range"]
        assert validation_error_body["msg"] == "Value error, 'start_date' should be less than or equal to 'end_date'"


@pytest.mark.parametrize(
    "payload",
    [
        {"filters": {"date_range": {"start_date": "2023-01-01", "end_date": "2024-01-01"}}},
        {"filters": {"category": ["Electronics", "Stationery"]}},
        {"filters": {"product_ids": [1001, 1002, 10016]}},
    ],
)
def test_optional_filters(payload, test_client):
    with test_client as client:
        req = client.post("/summary", json=payload)
    assert req.status_code == 200


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"columns": ["quantity_sold"]},
        {"columns": ["price_per_unit"]},
        {"columns": ["quantity_sold", "price_per_unit"]},
    ],
)
def test_dynamic_columns(payload, test_client):
    with test_client as client:
        req = client.post("/summary", json=payload)
    res = req.json()
    assert req.status_code == 200

    cols = payload.get("columns")
    if not cols:
        assert res
        assert len(res) > 0
    else:
        if len(cols) == 1:
            assert len(res) == 1
        for col in cols:
            assert col in res

import os

import pytest


@pytest.fixture(scope="session", autouse=True)
def override_env():
    os.environ["DATA_FILE_PATH"] = "tests/mocks/data.csv"
    assert os.environ.get("DATA_FILE_PATH") == "tests/mocks/data.csv"

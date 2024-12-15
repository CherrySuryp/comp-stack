import os.path

import pandas as pd
import pytest

MOCK_PATH = "tests/mocks/data.csv"


@pytest.fixture
def sample_dataframe():
    assert os.path.exists(MOCK_PATH)

    df = pd.read_csv(MOCK_PATH)
    df["date"] = pd.to_datetime(df["date"])
    return df

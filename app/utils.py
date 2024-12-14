import os
from functools import wraps

import pandas as pd

from app.config import config


def singleton(cls):
    instances = {}

    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class DataLoader:
    def __init__(self, file_path: str = config.DATA_FILE_PATH):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Couldn't open file {file_path}")
        self._file_path = file_path
        self._data = None

    def load(self):
        self._data = pd.read_csv(self._file_path, delimiter=",", parse_dates=["date"])

    @property
    def data(self) -> pd.DataFrame:
        return self._data

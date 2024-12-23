import os

from pydantic import FilePath
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # fmt: off
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.realpath(__file__)), "../.env"),
        env_file_encoding="utf-8"
    )
    # fmt: on

    DATA_FILE_PATH: FilePath = "sales_data.csv"


config = Config()

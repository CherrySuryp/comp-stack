from datetime import datetime

import pandas as pd


class DataFilter:
    @staticmethod
    def filter_by_date_range(df: pd.DataFrame, start_date: datetime.date, end_date: datetime.date) -> pd.DataFrame:
        start_date = datetime.strftime(start_date, "%Y-%m-%d")
        end_date = datetime.strftime(end_date, "%Y-%m-%d")
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
        return df

    @staticmethod
    def filter_by_categories(df: pd.DataFrame, categories: list[str]) -> pd.DataFrame:
        df = df[df["category"].isin(categories)]
        return df

    @staticmethod
    def filter_by_product_ids(df: pd.DataFrame, product_ids: list[int]) -> pd.DataFrame:
        df = df[df["product_id"].isin(product_ids)]
        return df

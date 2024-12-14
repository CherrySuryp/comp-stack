from datetime import datetime

import pandas as pd

from app.schema import Filters, Summary, Metrics


class Summarizer:
    @staticmethod
    def _filter_data(data: pd.DataFrame, filters: Filters) -> pd.DataFrame:
        if filters.date_range:
            start_date = datetime.strftime(filters.date_range.start_date, "%Y-%m-%d")
            end_date = datetime.strftime(filters.date_range.end_date, "%Y-%m-%d")
            data = data[(data["date"] >= start_date) & (data["date"] <= end_date)]
        if filters.category:
            data = data[data["category"].isin(filters.category)]
        if filters.product_ids:
            data = data[data["product_id"].isin(filters.product_ids)]
        return data

    @staticmethod
    def _summarize(data: pd.DataFrame, columns: list[str] | None = None) -> Summary:
        summary = {}
        if not columns:
            columns = data.columns

        for column in columns:
            if column not in data.columns or not pd.api.types.is_numeric_dtype(data[column]):
                continue

            summary[column] = Metrics(
                mean=data[column].mean(),
                median=data[column].median(),
                mode=data[column].mode()[0] if not data[column].mode().empty else None,
                std_dev=data[column].std(),
                percentile_25=data[column].quantile(0.25),
                percentile_75=data[column].quantile(0.75),
            )
        return summary

    def __call__(self, data: pd.DataFrame, filters: Filters | None = None, columns: list[str] | None = None) -> Summary:
        filtered = self._filter_data(data, filters) if filters else data
        return self._summarize(filtered, columns) if not filtered.empty else {}

import pandas as pd

from app.schema import Metrics


class DataSummarizer:
    @staticmethod
    def summarize(df: pd.DataFrame, columns: list[str]) -> dict[str, dict[str, float | int]]:
        summary = {}
        for column in columns:
            if column not in df.columns or not pd.api.types.is_numeric_dtype(df[column]):
                continue

            summary[column] = Metrics(
                mean=df[column].mean(),
                median=df[column].median(),
                mode=df[column].mode()[0] if not df[column].mode().empty else None,
                std_dev=df[column].std(),
                percentile_25=df[column].quantile(0.25),
                percentile_75=df[column].quantile(0.75),
            )
        return summary

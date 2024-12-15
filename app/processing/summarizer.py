import pandas as pd


class DataSummarizer:
    @staticmethod
    def summarize(df: pd.DataFrame, columns: list[str]) -> dict[str, dict[str, float | int]]:
        summary = {}
        for column in columns:
            if column not in df.columns or not pd.api.types.is_numeric_dtype(df[column]):
                continue
            summary[column] = dict(
                mean=df[column].mean(),
                median=df[column].median(),
                mode=df[column].mode()[0],
                std_dev=df[column].std(),
                percentile_25=df[column].quantile(0.25),
                percentile_75=df[column].quantile(0.75),
            )
        return summary

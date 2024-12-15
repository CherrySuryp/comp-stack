import pandas as pd

from app.schema import GetSummary, Summary, Filters
from app.processing.filter import DataFilter
from app.processing.summarizer import DataSummarizer
from app.utils import DataLoader


class SummaryGenerator:
    def __init__(
            self,
            data_loader: DataLoader = DataLoader(),
            data_filter: DataFilter = DataFilter(),
            summarizer: DataSummarizer = DataSummarizer(),
    ):
        self._data_loader = data_loader
        self._filter = data_filter
        self._summarizer = summarizer

    def _filter_data(self, df: pd.DataFrame, filters: Filters) -> pd.DataFrame:
        if filters.date_range:
            date_range = filters.date_range
            df = self._filter.filter_by_date_range(df, date_range.start_date, date_range.end_date)
        if filters.category:
            df = self._filter.filter_by_categories(df, filters.category)
        if filters.product_ids:
            df = self._filter.filter_by_product_ids(df, filters.product_ids)
        return df

    def _summarize_data(self, df: pd.DataFrame, columns: list[str] | None = None) -> Summary:
        if not columns:
            columns = df.columns
        return self._summarizer.summarize(df, columns)

    def _process(self, data: pd.DataFrame, filters: Filters | None = None, columns: list[str] | None = None) -> Summary:
        filtered = self._filter_data(data, filters) if filters else data
        return self._summarize_data(filtered, columns) if not filtered.empty else {}

    def __call__(self, body: GetSummary) -> Summary:
        data = self._data_loader.data
        return self._process(data, body.filters, body.columns)


make_summary = SummaryGenerator()

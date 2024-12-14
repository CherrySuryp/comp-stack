from app.schema import GetSummary, Summary
from app.service import DataLoader, Summarizer

data_loader = DataLoader()
summarizer = Summarizer()


def make_summary(body: GetSummary) -> Summary:
    data = data_loader.data
    summary = summarizer(data, body.filters, body.columns)
    return summary

import pytest

from app.processing import DataSummarizer


def test_summarize_numeric_columns(sample_dataframe):
    columns_to_summarize = ["quantity_sold", "price_per_unit"]
    summary = DataSummarizer.summarize(sample_dataframe, columns_to_summarize)

    # Expected summary for "quantity_sold"
    quantity_sold = sample_dataframe["quantity_sold"]
    assert summary["quantity_sold"]["mean"] == pytest.approx(quantity_sold.mean())
    assert summary["quantity_sold"]["median"] == pytest.approx(quantity_sold.median())
    assert summary["quantity_sold"]["mode"] == quantity_sold.mode()[0]
    assert summary["quantity_sold"]["std_dev"] == pytest.approx(quantity_sold.std())
    assert summary["quantity_sold"]["percentile_25"] == pytest.approx(quantity_sold.quantile(0.25))
    assert summary["quantity_sold"]["percentile_75"] == pytest.approx(quantity_sold.quantile(0.75))

    # Expected summary for "price_per_unit"
    price_per_unit = sample_dataframe["price_per_unit"]
    assert summary["price_per_unit"]["mean"] == pytest.approx(price_per_unit.mean())
    assert summary["price_per_unit"]["median"] == pytest.approx(price_per_unit.median())
    assert summary["price_per_unit"]["mode"] == price_per_unit.mode()[0]
    assert summary["price_per_unit"]["std_dev"] == pytest.approx(price_per_unit.std())
    assert summary["price_per_unit"]["percentile_25"] == pytest.approx(price_per_unit.quantile(0.25))
    assert summary["price_per_unit"]["percentile_75"] == pytest.approx(price_per_unit.quantile(0.75))


def test_ignores_non_numeric_columns(sample_dataframe):
    columns_to_summarize = ["quantity_sold", "price_per_unit", "product_name", "category"]
    summary = DataSummarizer.summarize(sample_dataframe, columns_to_summarize)

    # Only numeric columns should be present in the summary
    assert "product_name" not in summary
    assert "category" not in summary
    assert "quantity_sold" in summary
    assert "price_per_unit" in summary

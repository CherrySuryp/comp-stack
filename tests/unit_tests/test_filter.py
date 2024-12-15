from datetime import datetime

from app.processing import DataFilter


def test_filter_by_date_range(sample_dataframe):
    start_date = datetime(2023, 2, 1)
    end_date = datetime(2023, 3, 1)
    filtered_df = DataFilter.filter_by_date_range(sample_dataframe, start_date, end_date)

    # Expected product IDs: 1011 (Notebook), 1018 (Hair Dryer), and 1006 (Blender)
    assert set(filtered_df["product_id"]) == {1011, 1018, 1006}
    assert all((start_date <= row_date <= end_date) for row_date in filtered_df["date"])


def test_filter_by_categories(sample_dataframe):
    categories = ["Electronics", "Health & Beauty"]
    filtered_df = DataFilter.filter_by_categories(sample_dataframe, categories)

    # Expected categories only
    assert set(filtered_df["category"].unique()) <= set(categories)
    assert set(filtered_df["product_id"]) == {1016, 1017, 1009, 1018, 1002}


def test_filter_by_product_ids(sample_dataframe):
    product_ids = [1016, 1010, 1006]
    filtered_df = DataFilter.filter_by_product_ids(sample_dataframe, product_ids)

    # Expected product IDs only
    assert set(filtered_df["product_id"]) == set(product_ids)
    assert all(product_id in product_ids for product_id in filtered_df["product_id"])

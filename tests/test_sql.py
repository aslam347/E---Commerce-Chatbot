from unittest.mock import patch
import pandas as pd

import app.sql as sql


def test_run_query_returns_dataframe():
    sample_df = pd.DataFrame([{
        "title": "Nike Shoes",
        "price": 2999,
        "discount": 0.2,
        "avg_rating": 4.5,
        "product_link": "https://example.com"
    }])

    with patch("app.sql.pd.read_sql_query", return_value=sample_df):
        result = sql.run_query("SELECT * FROM product")

    assert result is not None
    assert not result.empty
    assert result.iloc[0]["title"] == "Nike Shoes"
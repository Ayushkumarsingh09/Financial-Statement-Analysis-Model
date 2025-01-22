import pytest
import pandas as pd
from src.trend_analysis import calculate_year_over_year_growth


def test_calculate_year_over_year_growth():
    financial_data = pd.DataFrame({
        "Year": [2020, 2021, 2022],
        "Revenue": [1000, 1200, 1500]
    }).set_index("Year")
    growth = calculate_year_over_year_growth(financial_data, "Revenue")
    assert growth.iloc[0] == pytest.approx(None)  # First value should be NaN
    assert growth.iloc[1] == 20  # 1200 -> 1000
    assert growth.iloc[2] == 25  # 1500 -> 1200

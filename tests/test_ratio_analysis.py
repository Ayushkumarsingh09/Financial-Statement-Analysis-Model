import pytest
import pandas as pd
from src.ratio_analysis import calculate_profitability_ratios, calculate_liquidity_ratios


@pytest.fixture
def sample_data():
    income_statement = pd.DataFrame({
        "Metric": ["Revenue", "Net Income"],
        "Value": [1000, 200]
    }).set_index("Metric")
    balance_sheet = pd.DataFrame({
        "Metric": ["Current Assets", "Inventory", "Current Liabilities", "Total Assets"],
        "Value": [500, 100, 300, 1500]
    }).set_index("Metric")
    return income_statement, balance_sheet


def test_calculate_profitability_ratios(sample_data):
    income_statement, balance_sheet = sample_data
    ratios = calculate_profitability_ratios(income_statement, balance_sheet)
    assert "Net Profit Margin" in ratios
    assert "Return on Assets (ROA)" in ratios
    assert ratios["Net Profit Margin"] == 0.2
    assert ratios["Return on Assets (ROA)"] == 0.1333


def test_calculate_liquidity_ratios(sample_data):
    _, balance_sheet = sample_data
    ratios = calculate_liquidity_ratios(balance_sheet)
    assert "Current Ratio" in ratios
    assert "Quick Ratio" in ratios
    assert ratios["Current Ratio"] == 1.6667
    assert ratios["Quick Ratio"] == 1.3333

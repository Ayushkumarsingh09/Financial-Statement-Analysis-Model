import pytest
from src.data_ingestion import load_financial_statements, preprocess_financial_data


def test_load_financial_statements():
    file_path = "tests/sample_data/financial_statements.xlsx"
    data = load_financial_statements(file_path)
    assert isinstance(data, dict)
    assert len(data) > 0  # Ensure data is loaded


def test_preprocess_financial_data():
    sample_data = {
        "Sheet1": {
            "Column A": ["  Revenue ", "  Net Income "],
            "Value": [1000, 200],
        }
    }
    df = preprocess_financial_data(sample_data)
    assert len(df) == 2 
    assert "Revenue" in df["Sheet1"].columns  # Ensure column names are cleaned
    assert df["Sheet1"].shape[0] > 0  # Ensure no rows were removed unnecessarily

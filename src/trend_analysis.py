def calculate_year_over_year_growth(financial_data, column_name):
    """
    Calculate year-over-year growth for a financial metric.

    Args:
        financial_data (pd.DataFrame): Financial data with years as index.
        column_name (str): Column to calculate growth for.

    Returns:
        pd.Series: Year-over-year growth percentages.
    """
    try:
        return financial_data[column_name].pct_change() * 100
    except Exception as e:
        raise Exception(f"Error calculating YoY growth: {e}")

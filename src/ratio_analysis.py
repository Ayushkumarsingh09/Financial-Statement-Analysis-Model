def calculate_profitability_ratios(income_statement, balance_sheet):
    """
    Calculate profitability ratios.

    Args:
        income_statement (pd.DataFrame): Income statement data.
        balance_sheet (pd.DataFrame): Balance sheet data.

    Returns:
        dict: Profitability ratios.
    """
    try:
        net_income = income_statement.loc["Net Income", "Value"]
        total_revenue = income_statement.loc["Revenue", "Value"]
        total_assets = balance_sheet.loc["Total Assets", "Value"]

        return {
            "Net Profit Margin": net_income / total_revenue,
            "Return on Assets (ROA)": net_income / total_assets,
        }
    except Exception as e:
        raise Exception(f"Error calculating profitability ratios: {e}")


def calculate_liquidity_ratios(balance_sheet):
    """
    Calculate liquidity ratios.

    Args:
        balance_sheet (pd.DataFrame): Balance sheet data.

    Returns:
        dict: Liquidity ratios.
    """
    try:
        current_assets = balance_sheet.loc["Current Assets", "Value"]
        current_liabilities = balance_sheet.loc["Current Liabilities", "Value"]

        return {
            "Current Ratio": current_assets / current_liabilities,
            "Quick Ratio": (current_assets - balance_sheet.loc["Inventory", "Value"])
            / current_liabilities,
        }
    except Exception as e:
        raise Exception(f"Error calculating liquidity ratios: {e}")

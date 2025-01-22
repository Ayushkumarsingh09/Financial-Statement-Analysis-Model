import pandas as pd


def load_financial_statements(file_path):
    """
    Load financial statements from an Excel file.

    Args:
        file_path (str): Path to the Excel file containing financial statements.

    Returns:
        dict: A dictionary of DataFrames with sheet names as keys.
    """
    try:
        data = pd.read_excel(file_path, sheet_name=None)
        return data
    except Exception as e:
        raise Exception(f"Error loading financial statements: {e}")


def preprocess_financial_data(data):
    """
    Perform basic preprocessing on financial data.

    Args:
        data (dict): Dictionary of DataFrames for financial statements.

    Returns:
        dict: Preprocessed DataFrames.
    """
    processed_data = {}
    for sheet, df in data.items():
        df = df.dropna(how="all")  # Drop completely empty rows
        df.columns = df.columns.str.strip()  # Strip whitespace from column names
        processed_data[sheet] = df
    return processed_data

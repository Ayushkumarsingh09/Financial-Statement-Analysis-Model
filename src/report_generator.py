def generate_report(ratios, file_path):
    """
    Generate a summary report of financial ratios.

    Args:
        ratios (dict): Dictionary of financial ratios.
        file_path (str): Path to save the report.
    """
    try:
        with open(file_path, "w") as f:
            f.write("Financial Ratios Summary Report\n")
            f.write("=" * 30 + "\n")
            for ratio, value in ratios.items():
                f.write(f"{ratio}: {value:.2f}\n")
    except Exception as e:
        raise Exception(f"Error generating report: {e}")

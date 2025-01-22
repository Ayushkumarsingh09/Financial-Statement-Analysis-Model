def safe_divide(numerator, denominator):
    """
    Safely divide two numbers.

    Args:
        numerator (float): The numerator.
        denominator (float): The denominator.

    Returns:
        float: The result or 0 if division by zero occurs.
    """
    try:
        return numerator / denominator if denominator != 0 else 0
    except Exception:
        return 0

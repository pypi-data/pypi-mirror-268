from datetime import datetime, timedelta

def calculate_remaining_time(end_date):
    """
    Calculate the remaining time until the rent payment deadline.

    Parameters:
        end_date (datetime): The end date of the rent payment period.

    Returns:
        timedelta: The remaining time until the payment deadline.
    """
    current_date = datetime.now()
    time_remaining = end_date - current_date
    return time_remaining

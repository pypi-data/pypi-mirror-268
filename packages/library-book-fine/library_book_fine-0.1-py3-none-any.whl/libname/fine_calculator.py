# utils/fine_calculator.py

from datetime import date

def calculate_fine(issued_date):
    """
    Calculates the fine for overdue books based on the issued date.

    :param issued_date: The date the book was issued.
    :return: The calculated fine amount.
    """
    # Define the fine rate (per day)
    fine_rate = 10  # $10 per day

    # Calculate the difference between today's date and the issued date
    days_overdue = (date.today() - issued_date).days

    # Calculate the fine amount
    fine_amount = max(0, days_overdue - 15) * fine_rate  # Fine starts after 15 days

    return fine_amount

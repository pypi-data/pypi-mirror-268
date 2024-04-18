# fine_calculator.py

def calculate_fine(days_overdue):
    # Calculate fine based on the number of days overdue
    if days_overdue <= 0:
        return 0  # No fine if not overdue
    elif days_overdue <= 15:
        return days_overdue * 10  # Fine of 10 rupees per day for the first 15 days
    else:
        return 15 * 10 + (days_overdue - 15) * 20  # After 15 days, fine doubles to 20 rupees per day

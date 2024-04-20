from datetime import datetime, timedelta

class RentCounter:
    def __init__(self, end_date):
        self.end_date = end_date

    def calculate_remaining_time(self):
        """
        Calculate the remaining time until the rent payment deadline.

        Returns:
            timedelta: The remaining time until the payment deadline.
        """
        current_date = datetime.now()
        time_remaining = self.end_date - current_date
        return time_remaining

# Example usage:
# end_date = datetime(2024, 5, 1)
# counter = RentCounter(end_date)
# remaining_time = counter.calculate_remaining_time()
# print("Remaining time:", remaining_time)

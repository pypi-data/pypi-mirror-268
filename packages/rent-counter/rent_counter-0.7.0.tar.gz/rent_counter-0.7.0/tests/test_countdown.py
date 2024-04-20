import unittest
from datetime import datetime, timedelta
from countf.countdown import calculate_remaining_time

class TestCountdown(unittest.TestCase):
    def test_remaining_time_future(self):
        end_date = datetime.now() + timedelta(days=7)  # End date 7 days from now
        remaining_time = calculate_remaining_time(end_date)
        self.assertIsInstance(remaining_time, timedelta)
        self.assertGreaterEqual(remaining_time.total_seconds(), 0)

    def test_remaining_time_past(self):
        end_date = datetime.now() - timedelta(days=7)  # End date 7 days ago
        remaining_time = calculate_remaining_time(end_date)
        self.assertIsInstance(remaining_time, timedelta)
        self.assertLessEqual(remaining_time.total_seconds(), 0)

    def test_remaining_time_present(self):
        end_date = datetime.now()  # End date is the current date
        remaining_time = calculate_remaining_time(end_date)
        self.assertIsInstance(remaining_time, timedelta)
        self.assertLessEqual(abs(remaining_time.total_seconds()), 1)

if __name__ == '__main__':
    unittest.main()
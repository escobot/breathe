import unittest
from entrypoint import calculate_premium_rate, calculate_debits


class MyTestCase(unittest.TestCase):

    def test_calculate_premium_rate_valid_values(self):
        self.assertEqual(calculate_premium_rate(gender='M', age=45, smoker='S'), 0.55)

    def test_calculate_premium_rate_invalid_values(self):
        self.assertEqual(calculate_premium_rate(gender='invalid', age=-1, smoker='invalid'), 0)

    def test_calculate_debits_valid_values(self):
        self.assertEqual(calculate_debits(health="[ANXIETY,HEART]", smoker='S', alcohol=25, bmi=30), 120)

    def test_calculate_debits_invalid_values(self):
        self.assertEqual(calculate_debits(health="[INVALID]", smoker='invalid', alcohol=-1, bmi=-1), 0)


if __name__ == '__main__':
    unittest.main()

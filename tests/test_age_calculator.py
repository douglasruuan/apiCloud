from unittest import TestCase
from rules.age_calculator import AgeCalculator


class AgeCalculatorTest(TestCase):
    def test_if_age_is_under_18(self):
        returned_message = AgeCalculator(17).calculator()

        expected_message = 'Your age is under 18.'
        self.assertEqual(returned_message, expected_message)

    def test_if_age_is_above_18(self):
        returned_message = AgeCalculator(18).calculator()

        expected_message = None
        self.assertEqual(returned_message, expected_message)

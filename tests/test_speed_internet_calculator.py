'''from unittest import TestCase
from rules.speed_internet_calculator import SpeedInternetCalculator
from dtos.internet_test_dto import InternetTest


class SpeedInternetCalculatorTest(TestCase):

    def test_internet_speed_download_bigger(self):
        speed_internet = InternetTest()
        speed_internet.download_speed = 51
        speed_internet.upload_speed = 45

        returned_result = SpeedInternetCalculator(50).internet_calculator()

        expected_returned = 1
        self.assertEqual(returned_result, expected_returned)
'''

from dtos.internetTestDto import InternetTest


class SpeedInternetCalculator:
    speed_internet: InternetTest

    def __init__(self, speed_internet: InternetTest):
        self.speed_internet = speed_internet

    def internet_calculator(self):
        sum_numbers = 0
        if self.speed_internet.download_speed > 50:
            sum_numbers += 1
        if self.speed_internet.upload_speed > 50:
            sum_numbers += 1
        if self.speed_internet.download_speed < 5:
            sum_numbers -= 1
        if self.speed_internet.upload_speed < 5:
            sum_numbers -= 1
        return sum_numbers

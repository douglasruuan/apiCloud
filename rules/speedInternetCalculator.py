from dtos.internetTestDto import InternetTest


class speedInternetCalculator:
    speed_internet: InternetTest

    def __init__(self, speed_internet: InternetTest):
        self.speed_internet = speed_internet

    def internetcalculator(self):
        sumNum = 0
        if self.speed_internet.download_speed > 50:
            sumNum += 1
        if self.speed_internet.upload_speed > 50:
            sumNum += 1
        if self.speed_internet.download_speed < 5:
            sumNum -= 1
        if self.speed_internet.upload_speed < 5:
            sumNum -= 1
        return sumNum

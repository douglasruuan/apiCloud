class wrtingScoreCalculator:
    wrting_score_code: float

    def __init__(self, wrting_score_code: float):
        self.wrting_score_code = wrting_score_code

    def calculatorWrting(self):
        scoreNum = 0

        if self.wrting_score_code < 0.3:
            scoreNum -= 1
        if self.wrting_score_code >= 0.3 and 0.7:
            scoreNum += 1
        if self.wrting_score_code > 0.7:
            scoreNum += 1

        return scoreNum

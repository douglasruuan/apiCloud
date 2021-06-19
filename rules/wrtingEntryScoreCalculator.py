class WrtingEntryScoreCalculator:
    wrting_entry_score: float

    def __init__(self, wrting_score_code: float):
        self.wrting_entry_score = wrting_score_code

    def calculator_entry_score(self):

        scoreNum = 0

        if self.wrting_entry_score < 0.3:
            scoreNum -= 1
        if self.wrting_entry_score >= 0.3 and 0.7:
            scoreNum += 1
        if self.wrting_entry_score > 0.7:
            scoreNum += 1

        return scoreNum

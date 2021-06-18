from dtos.pastExperienceDto import PastExperience


class ProSellOrSupport:
    past_experience: PastExperience

    def __init__(self, past_experience: PastExperience):
        self.past_experience = past_experience

    def calculatorSellSupport(self):

        if self.past_experience.sales and self.past_experience.support:
            return 8

        if self.past_experience.sales:
            return 5

        if self.past_experience.support:
            return 3
        return 0

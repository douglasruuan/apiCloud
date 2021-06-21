from rules.age_calculator import AgeCalculator
from rules.wrting_entry_score_calculator import WrtingEntryScoreCalculator
from rules.speed_internet_calculator import SpeedInternetCalculator
from rules.school_calculator import SchoolCalculator
from rules.pro_sell_or_support_calculator import ProSellOrSupportCalculator
from rules.referal_code_calculator import ReferralCodeCalculator
from dtos.output_result_dto import OutputResult
from dtos.input_job_pro_dto import JobPro


class CalculatingFinalResult:
    score = 0
    selectedProject = str

    def calculator_score(self, job_pro_dto: JobPro):
        message_age = AgeCalculator(job_pro_dto.age).calculator()

        if message_age is not None:
            return message_age
        self.score += SchoolCalculator(job_pro_dto.education_level).calculator_school()
        self.score += ProSellOrSupportCalculator(job_pro_dto.past_experiences).calculator_sell_or_support()
        self.score += SpeedInternetCalculator(job_pro_dto.internet_test).internet_calculator()
        self.score += WrtingEntryScoreCalculator(job_pro_dto.writing_score).calculator_entry_score()
        self.score += ReferralCodeCalculator(job_pro_dto.referral_code).calculator_referral_code()

        selectedproject = self.__project_selected()
        listproject = self.__project_results()
        eligiblelist = self.__project_eligible()

        return OutputResult(self.score, selectedproject, listproject, eligiblelist)

    def __project_results(self):
        projectlist = []
        if self.score > 10:
            projectlist.append('Calculate the Dark Matter of the universe for Nasa')
        if self.score > 5:
            projectlist.append('Determine if the Schrodinger s cat is alive')
        if self.score > 3:
            projectlist.append('Support for a YXZ Company')
        if self.score > 2:
            projectlist.append('Collect specific people information from their social media for XPTO Company')
        return projectlist

    def __project_selected(self):

        if self.score > 10:
            return 'Calculate the Dark Matter of the universe for Nasa'

        if self.score > 5:
            return 'Determine if the Schrodinger s cat is alive'

        if self.score > 3:
            return 'Support for a YXZ Company'

        if self.score > 2:
            return 'Collect_information_for_xpto'

    def __project_eligible(self):
        eligiblelist = []

        if self.score < 10:
            eligiblelist.append('Calculate the Dark Matter of the universe for Nasa')

        if self.score < 5:
            eligiblelist.append('Determine if the Schrodinger s cat is alive')

        if self.score < 3:
            eligiblelist.append('Support for a YXZ Company')

        if self.score < 2:
            eligiblelist.append('Collect specific people information from their social media for XPTO Company')

        return eligiblelist

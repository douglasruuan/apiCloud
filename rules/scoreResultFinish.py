from .ageScoreCalculator import AgeScoreCalculator
from .wrtingScoreCalculator import wrtingScoreCalculator
from .speedInternetCalculator import speedInternetCalculator
from .scoreHighSchoolCalculator import ScoreHighSchool
from .proSellOrSupportCalculator import ProSellOrSupport
from .referalCodeCalculator import referalCode
from dtos.calculateScoreResult import CalculateScoreResult
from dtos.jobProDto import JobPro


class score_result_finish:
    score = 0
    selectedProject = str

    def calculator_score(self, jobProDto: JobPro):
        mensagem = AgeScoreCalculator(jobProDto.age).calculator()

        if mensagem is not None:
            return mensagem
        self.score += ScoreHighSchool(jobProDto.education_level).calculator_school()
        self.score += ProSellOrSupport(jobProDto.past_experiences).calculatorSellSupport()
        self.score += speedInternetCalculator(jobProDto.internet_test).internetcalculator()
        self.score += wrtingScoreCalculator(jobProDto.writing_score).calculatorWrting()
        self.score += referalCode(jobProDto.referral_code).calcultaorreferalcode()

        selectedProject = self.__project_selected()
        listProject = self.__project_results()
        listInegible = self.__project_inable()

        return CalculateScoreResult(self.score, selectedProject, listProject, listInegible)

    def __project_results(self):
        listProject = []
        if self.score > 10:
            listProject.append('Calculate the Dark Matter of the universe for Nasa')
        if self.score > 5:
            listProject.append('Determine if the Schrodinger s cat is alive')
        if self.score > 3:
            listProject.append('Support for a YXZ Company')
        if self.score > 2:
            listProject.append('Collect specific people information from their social media for XPTO Company')
        return listProject

    def __project_selected(self):

        if self.score > 10:
            return 'Calculate the Dark Matter of the universe for Nasa'

        if self.score > 5:
            return 'Determine if the Schrodinger s cat is alive'

        if self.score > 3:
            return 'Support for a YXZ Company'

        if self.score > 2:
            return 'Collect_information_for_xpto'

    def __project_inable(self):
        listInegible = []

        if self.score < 10:
            listInegible.append('Calculate the Dark Matter of the universe for Nasa')

        if self.score < 5:
            listInegible.append('Determine if the Schrodinger s cat is alive')

        if self.score < 3:
            listInegible.append('Support for a YXZ Company')

        if self.score < 2:
            listInegible.append('Collect specific people information from their social media for XPTO Company')

        return listInegible

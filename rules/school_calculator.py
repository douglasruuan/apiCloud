class SchoolCalculator:
    education_level = str

    def __init__(self, education_level):
        self.education_level = education_level

    def calculator_school(self):

        if self.education_level == 'no_education':
            return 0

        if self.education_level == 'high_school':
            return 1

        if self.education_level == 'bachelors_degree_or_high':
            return 2
        return 0

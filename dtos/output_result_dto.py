class OutputResult:
    score: int
    selected_project: str
    eligible_projects: []
    ineligible_projects: []

    def __init__(self, score, selected_project, eligible_projects, ineligible_projects):
        self.score = score
        self.selected_project = selected_project
        self.eligible_projects = eligible_projects
        self.ineligible_projects = ineligible_projects

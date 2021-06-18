from dtos.jobProDto import JobPro
from rules.scoreResultFinish import score_result_finish

from fastapi import FastAPI

app = FastAPI()


@app.post("/jobPro")
async def create_jobPro(jobPro: JobPro):
    return score_result_finish().calculator_score(jobPro)

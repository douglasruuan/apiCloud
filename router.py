from dtos.input_job_pro_dto import JobPro
from rules.calculating_final_result import CalculatingFinalResult

from fastapi import FastAPI

app = FastAPI()


@app.post("/jobPro")
async def create_jobpro(jobpro: JobPro):
    return CalculatingFinalResult().calculator_score(jobpro)

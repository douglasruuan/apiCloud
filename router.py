from dtos.inputJobProDto import JobPro
from rules.calculatingFinalResult import CalculatingFinalResult

from fastapi import FastAPI

app = FastAPI()


@app.post("/jobPro")
async def create_jobpro(jobpro: JobPro):
    return CalculatingFinalResult().calculator_score(jobpro)

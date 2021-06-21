from pydantic import BaseModel  # Converter a Classe em JSON.

from dtos.past_experience_dto import PastExperience
from dtos.internet_test_dto import InternetTest


class JobPro(BaseModel):
    age: int
    education_level: str
    past_experiences: PastExperience
    internet_test: InternetTest
    writing_score: float
    referral_code: str

from pydantic import BaseModel


class PastExperience(BaseModel):
    sales: bool
    support: bool

from pydantic import BaseModel


class InternetTest(BaseModel):
    download_speed: float
    upload_speed: float

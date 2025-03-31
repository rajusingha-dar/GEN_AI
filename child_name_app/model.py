from pydantic import BaseModel

class NameRequest(BaseModel):
    country: str
    gender: str
    language: str
    letter: str
    temperature: float
    sibling_name: str
    description: str

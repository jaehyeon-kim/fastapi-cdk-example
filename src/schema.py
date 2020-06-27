from typing import List
from pydantic import BaseModel


class Company(BaseModel):
    index: int
    company: str


class Companies(BaseModel):
    limit: int
    offset: int
    companies: List[Company]


class BasicError(BaseModel):
    detail: str

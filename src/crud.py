import os
import json
from typing import List, Dict
from src.schema import Company


def get_init_data():
    base_path = os.path.join(os.getcwd(), "data")
    with open(os.path.join(base_path, "companies.json"), "r") as f:
        companies = json.load(f)
    with open(os.path.join(base_path, "people.json"), "r") as f:
        people = json.load(f)
    return {"companies": companies, "people": people}


def get_companies(limit: int, offset: int, companies: List[Company]):
    return companies[offset : (limit + offset)]


def get_company(index: str, companies: List[Company]):
    try:
        return next(iter(com for com in companies if com["index"] == index))
    except StopIteration:
        return None

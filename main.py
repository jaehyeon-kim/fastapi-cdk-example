from typing import List, Dict
from fastapi import FastAPI, HTTPException, Query, Path, Depends
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from src import crud, schema

app = FastAPI(title="FastApi Example Api", version="0.0.1")
handler = Mangum(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def init_data():
    data = crud.get_init_data()
    yield data


@app.get(
    "/companies", response_model=schema.Companies, tags=["company"], summary="Get all companies"
)
def get_companies(
    limit: int = Query(10, ge=0, description="number of records to query"),
    offset: int = Query(0, ge=0, description="records offset"),
    data: Dict[List, List] = Depends(init_data),
):
    companies = crud.get_companies(limit, offset, data["companies"])
    return {"limit": limit, "offset": offset, "companies": companies}


@app.get(
    "/company/{company_id}",
    response_model=schema.Company,
    responses={"404": {"model": schema.BasicError}},
    summary="Get company give company id",
)
def get_company(
    company_id: int = Path(..., ge=0, le=99, description="company id"),
    data: Dict[List, List] = Depends(init_data),
):
    company = crud.get_company(company_id, data["companies"])
    print(company)
    if not company:
        raise HTTPException(404, detail="company not found")
    return company

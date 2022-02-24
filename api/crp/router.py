from typing import List

from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session


from api import db
from scrapper.crp_scrapper import CRPScrapper
from . import schemas, services
from scrapper import config

router = APIRouter(tags=['CRP Validation'], prefix='/crp')


@router.post("/validate")
async def validate_crp(input_data: schemas.CRPRegisterValidationInput):
    scrapper = CRPScrapper(config=config.ScrapperConfig)
    data = scrapper.scrape_for_user_data(register=input_data.crp_register, cpf=input_data.cpf)
    if data is None:
        return {"Message": "can't validate crp register"}

    return data

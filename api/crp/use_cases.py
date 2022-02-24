from typing import Optional

from fastapi import (
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from api.crp import (
    models,
    schemas,
    services,
)
from scrapper.crp_scrapper import CRPScrapper


async def get_data_from_db_use_case(request: schemas.CRPRegisterValidationInput, database: Session) -> Optional[
    models.CRPUser
]:
    crp_user_data = await services.get_crp_user_by_cpf(request.cpf, database)
    return crp_user_data


async def get_data_from_web_scrapper_use_case(
    request: schemas.CRPRegisterValidationInput,
    database: Session,
    scrapper: CRPScrapper
) -> models.CRPUser:
    crp_user_data = scrapper.scrape_for_user_data(register=request.crp_register, cpf=request.cpf)
    if crp_user_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not found any data from inputted data."
        )

    user_data = await services.create_or_update_crp_user(crp_user_data, database)
    return user_data

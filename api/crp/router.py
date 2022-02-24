from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.orm import Session

from api import db
from . import (
    schemas,
    use_cases,
)
from scrapper import get_scrapper

router = APIRouter(tags=['CRP Validation'], prefix='/crp')


@router.post("/", response_model=schemas.CRPUserData)
async def validate_crp(
    request: schemas.CRPRegisterValidationInput,
    database: Session = Depends(db.get_db),
):
    data = await use_cases.get_data_from_db_use_case(request, database)
    if data is None:
        scrapper = get_scrapper()
        data = await use_cases.get_data_from_web_scrapper_use_case(request, database, scrapper)
        del scrapper

    return data

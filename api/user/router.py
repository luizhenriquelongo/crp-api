from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Response,
)
from sqlalchemy.orm import Session
from api import db
from . import (
    schemas,
    services,
)

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schemas.User, database: Session = Depends(db.get_db)):
    return await services.create_new_user(request, database)


@router.get('/', response_model=List[schemas.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.get_all_users(database)


@router.get('/{user_id}', response_model=schemas.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_user(user_id, database)

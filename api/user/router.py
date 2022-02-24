from typing import List

from fastapi import (
    APIRouter,
    Depends,
    status,
    Response,
    HTTPException,
)
from sqlalchemy.orm import Session
from api import db
from . import (
    schemas,
    services,
    validator,
)

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schemas.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail='The user with this email already exists in the system.'
        )

    new_user = await services.register_new_user(request, database)
    return new_user


@router.get('/', response_model=List[schemas.DisplayUser])
async def get_all_users(database: Session = Depends(db.get_db)):
    return await services.get_all_users(database)


@router.get('/{user_id}', response_model=schemas.DisplayUser)
async def get_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.get_user_by_id(user_id, database)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(user_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_user_by_id(user_id, database)

from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.user import (
    models,
    schemas,
    validator,
    dao,
)


async def create_new_user(request: schemas.User, database: Session) -> models.User:
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(
            status_code=400,
            detail='The user with this email already exists in the system.'
        )

    new_user = await dao.register_new_user(request, database)
    return new_user


async def get_all_users(database: Session) -> List[models.User]:
    return await dao.get_all_users(database)


async def get_user(user_id: int, database: Session) -> models.User:
    return await dao.get_user_by_id(user_id, database)


async def delete_user(user_id: int, database: Session):
    return await dao.delete_user_by_id(user_id, database)

from typing import Optional

from sqlalchemy.orm import Session

from . import (
    schemas,
    models,
)


async def get_crp_user_by_cpf(cpf: str, database: Session) -> Optional[models.CRPUser]:
    return database.query(models.CRPUser).filter(models.CRPUser.cpf == cpf).first()


async def create_or_update_crp_user(user_data: schemas.CRPUserData, database: Session) -> models.CRPUser:
    crp_user = await get_crp_user_by_cpf(user_data.cpf, database)
    if crp_user is not None:
        crp_user.name = user_data.name
        crp_user.region = user_data.region
        crp_user.register_number = user_data.register_number
        crp_user.register_status = user_data.register_status
        crp_user.is_active = user_data.is_active

    else:
        crp_user = models.CRPUser(**user_data.dict())
        database.add(crp_user)

    database.commit()
    database.refresh(crp_user)
    return crp_user

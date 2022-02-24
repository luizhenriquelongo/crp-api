from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

from api.db import Base


class CRPUser(Base):
    __tablename__ = "crp_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(String(12), unique=True)
    name = Column(String(255))
    region = Column(String(255))
    register_number = Column(String(255))
    register_status = Column(String(255))
    is_active = Column(Boolean)

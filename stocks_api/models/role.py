from .association import Roles_Association
from .meta import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
)


class AccountRole(Base):
    __tablename__ = 'account_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)

    accounts = relationship('Account', secondary=Roles_Association, back_populates='roles')


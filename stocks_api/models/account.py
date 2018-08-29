from .portfolio import Portfolio
from .role import AccountRole
from .association import Roles_Association
from .meta import Base
from datetime import datetime as dt
from sqlalchemy.orm import relationship
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Text,
    Index,
    Integer,
    String,
    DateTime,
)


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    portfolio = relationship(Portfolio, back_populates='account')
    roles = relationship(AccountRole, secondary=Roles_Association, back_populates='accounts')

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = password

    @classmethod
    def new(cls, request, email=None, password=None):
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()

    @classmethod
    def check_credentials(cls, request, email, password):
        pass


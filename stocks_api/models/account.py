from .association import roles_association
from cryptacular import bcrypt
from datetime import datetime as dt
from .meta import Base
from .portfolio import Portfolio
from .role import AccountRole
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

manager = bcrypt.BCRYPTPasswordManager()


class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    # username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    portfolio = relationship(Portfolio, back_populates='accounts')
    roles = relationship(AccountRole, secondary=roles_association, back_populates='accounts')

    def __init__(self, email=None, password=None):
        self.email = email
        self.password = manager.encode(password, 10)

    @classmethod
    def new(cls, request, email=None, password=None):
        if request.dbsession is None:
            raise DBAPIError

        user = cls(email, password)
        request.dbsession.add(user)

        # TODO: Assign roles to new user

        admin_role = request.dbsession.query(AccountRole).filter(
            AccountRole.name == 'admin').one_or_none())

        user.roles.append(admin_role)
        request.dbsession.flush()

        return request.dbsession.query(cls).filter(cls.email == email).one_or_none()


    @classmethod
    def one(cls, request, email=None):
        return request.dbsession.query(cls).filter(
            cls.email == email).one_or_none()


    @classmethod
    def check_credentials(cls, request, email, password):
        if request.dbsession is None:
            raise DBAPIError

        try:
            account = request.dbsession.query(cls).filter(cls.email == email).one_or_none()
        except DBAPIError:
            return None

        if account is not None:
            if manager.check(account.password, password):
                return account
        return None


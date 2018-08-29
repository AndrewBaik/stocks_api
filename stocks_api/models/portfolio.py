from .stock import Stock
from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Index,
    Text,
    Integer,
    DateTime,
    ForeignKey,
)
from .meta import Base


class Portfolio(Base):
    """ Creating a new Portfolio table for the database
    """
    __tablename__ = 'portfolio'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_created = Column(DateTime, default=dt.now())
    date_udpated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    account_id = Column(Integer, ForeignKey('accounts.id'))
    accounts = relationship('Account', back_populates='portfolio')
    stock = relationship(Stock, back_populates='portfolio')

    @classmethod
    def new(cls, request=None, **kwargs):
        """ Method for creating a new row in portfolio
        """
        if request is None:
            raise DBAPIError

        portfolio = cls(**kwargs)
        request.dbsession.add(portfolio)
        return request.dbsession.query(cls).filter(
            cls.name == kwargs['name']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """ Method for displaying selected row
        """
        if request is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(
            cls.id == pk)

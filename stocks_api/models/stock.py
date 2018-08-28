from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy import (
    Column,
    Text,
    DateTime,
    Integer,
    Index,
)
from .meta import Base


class Stock(Base):
    """ Creating a new Stock table for the database
    """
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    companyName = Column(Text)
    exchange = Column(Text)
    industry = Column(Text)
    website = Column(Text)
    description = Column(Text)
    CEO = Column(Text)
    issueType = Column(Text)
    sector = Column(Text)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)

    @classmethod
    def new(cls, request=None, **kwargs):
        """ Create a new row in Stock
        """
        if request is None:
            raise DBAPIError
        stock = cls(**kwargs)
        request.dbsession.add(stock)
        return request.dbsession.query(cls).filter(
            cls.symbol == kwargs['symbol']).one_or_none()

    @classmethod
    def one(cls, request=None, pk=None):
        """ Retrieve selected row from Stock
        """
        if request is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(
            cls.symbol == pk)

    @classmethod
    def remove(cls, request=None, pk=None):
        """ Delete a selected row from Stock
        """
        if request is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(
            cls.id == pk).delete()


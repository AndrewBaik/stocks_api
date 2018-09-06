from datetime import datetime as dt
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Text,
    DateTime,
    Integer,
    Index,
    ForeignKey,
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
    date_created = Column(DateTime, default=dt.now())
    date_updated = Column(DateTime, default=dt.now(), onupdate=dt.now())

    portfolio_id = Column(Integer, ForeignKey('portfolio.id'))
    portfolio = relationship('Portfolio', back_populates='stock')

    @classmethod
    def all(cls, request):
        """ return all of stock data
        """
        if request.dbsession is None:
            raise DBAPIError

        return request.dbsession.query(cls).all()

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
        # import pdb; pdb.set_trace()
        if request is None:
            raise DBAPIError
        return request.dbsession.query(cls).filter(
            cls.id == pk).one_or_none()

    @classmethod
    def remove(cls, request=None, pk=None):
        """ Delete a selected row from Stock
        """
        if request is None:
            raise DBAPIError

        return request.dbsession.query(cls).filter(
            cls.accounts.email == request.authenticated_userid).filter(cls.id == pk).delete()


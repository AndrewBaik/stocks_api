from marshmallow_sqlalchemy import ModelSchema
from .portfolio import Portfolio
from .stock import Stock


class PortfolioSchema(ModelSchema):
    """ serializing Portforlio using marshmallow sqlalchemy
    """
    class meta:
        model = Portfolio


class StockSchema(ModelSchema):
    """ serializing stock using marshmallow sqlalchemy
    """
    class meta:
        model = Stock

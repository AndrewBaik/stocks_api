from marshmallow_sqlalchemy import ModelSchema
from .portfolio import Portfolio
from .stock import Stock


class PortfolioSchema(ModelSchema):
    class meta:
        model = Portfolio


class StockSchema(ModelSchema):
    class meta:
        model = Stock

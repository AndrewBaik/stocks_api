from marshmallow_sqlalchemy import ModelSchema
from marshmallow_sqlalchemy.fields import fields
from . import Portfolio, Stock
from .role import AccountRole
from .association import roles_association
from .account import Account


class RoleAssociationSchema(ModelSchema):
    class Meta:
        model = roles_association


class AccountRoleSchema(ModelSchema):
    class Meta:
        model = AccountRole


class AccountSchema(ModelSchema):
    role = fields.Nested(AccountRoleSchema, many=True, only='name')

    class Meta:
        model = Account


class PortfolioSchema(ModelSchema):
    """ serializing Portforlio using marshmallow sqlalchemy
    """
    roles = fields.Nested(AccountRoleSchema, many=True, only='name')
    account = fields.Nested(AccountSchema, exclude=('password', 'locations', 'roles', 'data_created', 'date_updated'))

    class meta:
        model = Portfolio


class StockSchema(ModelSchema):
    """ serializing stock using marshmallow sqlalchemy
    """
    portfolio = fields.Nested(PortfolioSchema)

    class meta:
        model = Stock

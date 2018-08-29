from sqlalchemy import Table, Column, Integer, ForeignKey
# from sqlalchemy.orm import relationship
from .meta import metadata


roles_association = Table(
    'roles_association',
    metadata,
    Column('account_id', Integer, ForeignKey('accounts.id')),
    Column('role_id', Integer, ForeignKey('account_roles.id'))
)

# class Roles_Association(Base):
#     __tablename__ = 'roles_association'
#     id = Column(Text, primary_key=True)

#     account_id = Column(Integer, ForeignKey('accounts.id'))
#     # account = relationship('Account', back_populates='role_association')

#     role_id = Column(Integer, ForeignKey('account_roles.id'))
#     # account_role = relationship('AccountRole', back_populates='roles_association')

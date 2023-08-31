#!/usr/bin/python3

""" This module holds the code for the creation of a account class """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, Table, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

account_transaction = Table('account_transaction', Base.metadata,
                          Column('account_id', String(60),
                                 ForeignKey('accounts.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('transaction_id', String(60),
                                 ForeignKey('transactions.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Account(BaseModel, Base):
    """ This are attributes for all account objects """

    __tablename__ = 'accounts'
    account_number = Column(String(128), nullable=False)
    amount_account = Column(Float)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    transactions = relationship("Transaction", secondary="account_transaction",
                                 cascade="all, delete",
                                 backref="account_transactions",
                                 viewonly=False)

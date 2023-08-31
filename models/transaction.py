#!/usr/bin/python3

""" This module holds the code for the creation of a transaction class """

from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Table, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
from sqlalchemy.orm import relationship
from os import getenv


class Transaction(BaseModel, Base):
    """ This are attributes for all transactions objects """

    __tablename__ = "transactions"
    account_id = Column(String(60), ForeignKey("accounts.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    amount_transaction = Column(Float)
    description = Column(String(128))
    transaction_type = Column(Integer,  default=0)

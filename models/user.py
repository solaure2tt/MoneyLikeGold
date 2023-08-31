#!/usr/bin/python3

""" This module holds the code for the creation of a user class """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import shlex
from os import getenv
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ This are attributes for all user objects """

    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128))
    first_name = Column(String(128))
    last_name = Column(String(128))
    address = Column(String(128))
    phone = Column(String(128))
    if getenv("MLG_TYPE_STORAGE") == "db":
        accounts = relationship("Account", cascade='all, delete, delete-orphan',
                              backref="user")
        transactions = relationship("Transaction", cascade='all, delete, delete-orphan',
                              backref="user")
    else:
        @property
        def accounts(self):
            accounts = []
            tmp = []
            ms = models.storage.all()
            for key in models.storage.all():
                ac = key.replace('.', ' ')
                account = shlex.split(ac)
                if (account[0] == 'Account'):
                    tmp.append(ms[key])
            for obj in tmp:
                if (obj.user_id == self.id):
                    accounts.append(obj)
            return (accounts)

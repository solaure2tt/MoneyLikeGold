#!/usr/bin/python3
""" This module is to create the DB storage engine """
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.account import Account
from models.transaction import Transaction
from models.base_model import Base
name_classes = {
    'User': User,
    'Account': Account,
    'Transaction': Transaction
}


class DBStorage:
    """creation of the class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """instanciaton of the DBStorage"""
        user = getenv("MLG_MYSQL_USER")
        passw = getenv("MLG_MYSQL_PWD")
        db = getenv("MLG_MYSQL_DB")
        host = getenv("MLG_MYSQL_HOST")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passw, host, db),
                                      pool_pre_ping=True)
        if getenv("MLG_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return all objects depending of the class name cls"""
        res = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                res[key] = obj
        else:
            cl = [User, Account, Transaction]
            for c in cl:
                query = self.__session.query(c)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    res[key] = obj
        return (res)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add a new object in the table"""
        if obj:
            self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database and database session"""
        Base.metadata.create_all(self.__engine)
        s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s)
        self.__session = Session()

    def close(self):
        """close the session"""
        self.__session.close()

    def get(self, cls, id):
        """Retrieve an object"""
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in name_classes:
            cls = name_classes[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        '''class (optional)'''
        return (len(self.all(cls)))

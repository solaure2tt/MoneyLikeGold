#!/usr/bin/python3
"""This module create the base model of every objects in the application"""
from datetime import datetime
import uuid
import sys
import os
import json
import models as m
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
import MySQLdb


Base = declarative_base()



class BaseModel:
    """implement the base class of every objects"""
    if os.getenv("MLG_TYPE_STORAGE") == 'db':
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ This is the constructor for our class instances """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, val in kwargs.items():
                if key == 'updated_at' or key == 'created_at':
                    val = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, val)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        """if kwargs is not None and kwargs != {}:
            try:
                self.id = kwargs['id']
                created_at = kwargs['created_at']
                upd_at = kwargs['updated_at']
                self.created_at = dt.datetime.fromisoformat(created_at)
                self.updated_at = dt.datetime.fromisoformat(upd_at)
                for key, val in kwargs.items():
                    if key != '__class__':
                        setattr(self, key, val)
            except Exception as e:
                pass
        else:
            self.id = str(uuid.uuid4())
            self.created_at = dt.datetime.now()
            self.updated_at = dt.datetime.now()"""

    def save(self):
        """ This method updates the instance attribut updated_at """

        self.updated_at = datetime.now()
        m.storage.new(self)
        m.storage.save()

    def to_dict(self):
        """ This method returns a dict of key-value pairs as per the
        __dict__ builtin of the instance """

        dictionary = dict(self.__dict__)
        dictionary["__class__"] = str(type(self).__name__)
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def __str__(self):
        """ This method returns the string representation of any class
        instance """

        str_rep = "[{}] ({}) ".format(type(self).__name__, self.id)
        str_rep += "{}".format(self.__dict__)

        return str_rep

    def delete(self):
        """delete the current instance from the storage"""
        m.storage.delete(self)

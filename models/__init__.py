#!/usr/bin/python3
"""This module create a unique FileStorage
instance for the application"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.account import Account
from models.transaction import Transaction
import os


if os.getenv("MLG_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()

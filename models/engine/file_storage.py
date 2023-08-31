#!/usr/bin/python3

""" This module holds the code for a filestorage class """
import os
import json
import sys
import shlex
import datetime as dt
from models.base_model import BaseModel
from models.user import User
from models.account import Account
from models.transaction import Transaction


class FileStorage:
    """ This isclass serializes instance to a JSON file and vice versa """

    __file_path = "./file.json"
    __objects = {}

    def all(self, cls=None):
        """ This method returns the dictionary 
            of models cls currently in storage
        """
        res = {}
        if cls is not None:
            for key, obj in self.__objects.items():
                part = key.replace('.', ' ')
                part = shlex.split(part)
                if (part[0] == cls.__name__):
                    res[key] = self.__objects[key]
                """if cls  == obj.__class__:
                    res[key] = obj"""
            return res

        return FileStorage.__objects

    def new(self, obj):
        """ This method inserts obj in the __object dict
        Args:
            obj: list of objects
        """

        if obj is not None:
            try:
                key = type(obj).__name__ + '.' + obj.id
                FileStorage.__objects[key] = obj
            except Exception as e:
                print(e)

    def save(self):
        """ This method serializes __objects to __file_path """

        with open(FileStorage.__file_path, 'w') as file:
            if FileStorage.__objects is None:
                file.write("[]")
            else:
                ins = {}
                all_objs = self.all()
                for obj_id in all_objs.keys():
                    obj = all_objs[obj_id]
                    my_model_json = {"__class__": type(obj).__name__}
                    for key, value in obj.__dict__.items():
                        if isinstance(value, dt.datetime):
                            my_model_json[key] = value.isoformat()
                        else:
                            my_model_json[key] = value
                    ins[obj_id] = my_model_json
                file.write(json.dumps(ins, default=str))

    def reload(self):
        """ This method deserializes a JSON obeject to class object """

        class_list = ["BaseModel", "User", "Account", "Transaction"]

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                listDict = json.load(file)
                obj = {}
                for di in listDict:
                    obj[di] = listDict[di]
                if obj is not None:
                    for k in obj.keys():
                        ob = obj[k]
                        ob_class = ob['__class__']
                        key = ob['__class__'] + '.' + ob['id']
                        if ob_class in class_list:
                            FileStorage.__objects[key] = eval(ob_class)(**ob)

    def delete(self, obj=None):
        """delete obj from __objects if it exist"""
        if obj is not None:
            key = type(obj).__name__ + '.' + obj.id
            FileStorage.__objects.pop(key)

    def get(self, cls, id):
        '''object to get'''
        if cls and id:
            takeObj = '{}.{}'.format(cls, id)
            everyObj = self.all(cls)
            return everyObj.get(takeObj)
        else:
            return None

    def count(self, cls=None):
        '''class that is (optional)'''
        return (len(self.all(cls)))

#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.account import Account
from models.transaction import Transaction


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user2 = User()
my_user2.first_name = "Lor"
my_user2.email = "laure@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("-- Create a new account --")
my_account = Account()
my_account.account_number = "4587-7878-9696"
my_account.account_amount = 1500
my_account.user_id = my_user2.id
my_account.save()
print(my_account)

print("-- Create a new transaction --")
my_trans = Transaction()
my_trans.description = "wallmart groeceries"
my_trans.transaction_amount = 400
my_trans.transaction_type = 1
my_trans.account_id = my_account.id
my_trans.save()
print(my_trans)

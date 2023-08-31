#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.account import Account

print("All objects: {}".format(storage.count()))
print("Accounts objects: {}".format(storage.count(Account)))

first_acc_id = list(storage.all(Account).values())[0].id
print("first accound id: {}".format(first_acc_id))
print("First account: {}".format(storage.get("Account", first_acc_id)))

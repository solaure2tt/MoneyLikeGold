#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.transaction import Transaction

fs = FileStorage()

# All transactions
all_trans = fs.all(Transaction)
print("All Transactions: {}".format(len(all_trans.keys())))
for trans_key in all_trans.keys():
    print(all_trans[trans_key])

# Create a new Transaction
my_trans = Transaction()
my_trans.description = "frescho groeceries"
my_trans.transaction_amount = 800
my_trans.transaction_type = 1
my_trans.save()
print("New Transaction: {}".format(my_trans))

# All States
all_trans = fs.all(Transaction)
print("All Transactions: {}".format(len(all_trans.keys())))
for trans_key in all_trans.keys():
    print(all_trans[trans_key])

# Create another Transaction
my_trans = Transaction()
my_trans.description = "Airbnb alymer"
my_trans.transaction_amount = 150
my_trans.transaction_type = 1
my_trans.save()
print("New Transaction: {}".format(my_trans))

# All Transactions
all_trans = fs.all(Transaction)
print("All Transactions: {}".format(len(all_trans.keys())))
for trans_key in all_trans.keys():
    print(all_trans[trans_key])        

# Delete the new Transaction
fs.delete(my_trans)

# All Transactions
all_trans = fs.all(Transaction)
print("All Transactions: {}".format(len(all_trans.keys())))
for trans_key in all_trans.keys():
    print(all_trans[trans_key])

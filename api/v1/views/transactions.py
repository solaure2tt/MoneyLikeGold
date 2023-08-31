#!/usr/bin/python3
""" RestFul API actions for Accounts """
from models.user import User
from models.account import Account
from models.transaction import Transaction
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage


@app_views.route('/transactions', methods=['GET'], strict_slashes=False)
def get_transactions():
    """Retrieves the list of all transactions objects
    """
    all_transactions = storage.all(Transaction).values()
    list_transactions = []
    for trans in all_transactions:
        list_transactions.append(trans.to_dict())
    return jsonify(list_transactions)


@app_views.route('/transactions/<transaction_id>', methods=['GET'], strict_slashes=False)
def get_transaction(transaction_id):
    """ Retrieves an transaction """
    transaction = storage.get("Transaction", transaction_id)
    if not transaction:
        abort(404)

    return jsonify(transaction.to_dict())


@app_views.route('/account/<string:account_id>/transactions', methods=['GET'], strict_slashes=False)
def get_account_transactions(account_id):
    """ Retrieves all transaction for a specific account """
    account = storage.get("Account", account_id)
    if not account:
        abort(404)
    transactions = storage.all(Transaction).values()
    res = []
    for trans in transactions:
        if trans.account_id == account_id:
            res.append(trans.to_dict())
    return jsonify(res)


@app_views.route('/user/<string:user_id>/transactions', methods=['GET'], strict_slashes=False)
def get_user_transactions(user_id):
    """ Retrieves all transaction for a specific user """
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    transactions = storage.all(Transaction).values()
    res = []
    for trans in transactions:
        if trans.user_id == user_id:
            res.append(trans.to_dict())
    return jsonify(res)


@app_views.route('/transactions', methods=['POST'], strict_slashes=False)
def post_transaction():
    """
    Creates a transaction
    """
    wargs = {}
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    kwargs = request.get_json()
    if 'amount_transaction' not in kwargs:
        return make_response(jsonify({'error': 'Missing amount transaction'}), 400)
    if 'user_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing user_id'}), 400)
    user = storage.get("User", kwargs['user_id'])
    if user is None:
        abort(404)
    if 'account1_id' not in kwargs:
        return make_response(jsonify({'error': 'Missing account id'}), 400)
    account1 = storage.get("Account", kwargs['account1_id'])
    if account1 is None:
        abort(404)
    wargs['account_id'] = kwargs['account1_id']
    wargs['user_id'] = kwargs['user_id']
    if 'transaction_type' not in request.get_json():
        abort(400, description="Missing type of the transaction (0:W/D or 1:Tr")
    if kwargs['transaction_type'] == 0:
        wargs['transaction_type'] = 0
        wargs['amount_transaction'] = (-1) * kwargs['amount_transaction']
        account1.amount_account -= kwargs['amount_transaction']
        account1.save();
        trans = Transaction(**wargs)
        trans.save()
        return make_response(jsonify(trans.to_dict()), 201)
    if kwargs['transaction_type'] == 1:
        wargs['transaction_type'] = 1
        wargs['amount_transaction'] = kwargs['amount_transaction']
        account1.amount_account += kwargs['amount_transaction']
        account1.save();
        trans = Transaction(**wargs)
        trans.save()
        return make_response(jsonify(trans.to_dict()), 201)
    if kwargs['transaction_type'] == 2:
        if 'account2_id' not in kwargs:
            return make_response(jsonify({'error': 'Missing second account id'}), 400)
        account2 = storage.get("Account", kwargs['account2_id'])
        if account2 is None:
            abort(404)
        wargs['transaction_type'] = 2
        wargs['account_id'] = kwargs['account2_id']
        wargs['amount_transaction'] = kwargs['amount_transaction']
        account2.amount_account += kwargs['amount_transaction']
        account2.save();
        trans1 = Transaction(**wargs)
        wargs['amount_transaction'] = (-1) * kwargs['amount_transaction']
        wargs['account_id'] = kwargs['account1_id']
        account1.amount_account -= kwargs['amount_transaction']
        account1.save();
        trans2 = Transaction(**wargs)
        trans1.save()
        trans2.save()
        return make_response(jsonify(trans1.to_dict()), 201)
    return make_response(jsonify({'error': 'bad transaction type'}), 400)


@app_views.route('/transactions/<transaction_id>', methods=['PUT'], strict_slashes=False)
def put_transaction(transaction_id):
    """
    Updates a transaction
    """
    transaction = storage.get("Transaction", transaction_id)

    if not transaction:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(transaction, key, value)
    storage.save()
    return make_response(jsonify(transaction.to_dict()), 200)


@app_views.route('/transactions/<transaction_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_transaction(transaction_id):
    """
    Deletes a transaction Object
    """

    transaction = storage.get("Transaction", transaction_id)

    if not transaction:
        abort(404)

    storage.delete(transaction)
    storage.save()

    return make_response(jsonify({}), 200)

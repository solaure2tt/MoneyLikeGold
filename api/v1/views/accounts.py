#!/usr/bin/python3
""" RestFul API actions for Accounts """
from models.user import User
from models.account import Account
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage


@app_views.route('/accounts', methods=['GET'], strict_slashes=False)
def get_accounts():
    """Retrieves the list of all accounts objects
    """
    all_accounts = storage.all(Account).values()
    list_accounts = []
    for ac in all_accounts:
        list_accounts.append(ac.to_dict())
    return jsonify(list_accounts)


@app_views.route('/accounts/<account_id>', methods=['GET'], strict_slashes=False)
def get_account(account_id):
    """ Retrieves an account """
    account = storage.get("Account", account_id)
    if not account:
        abort(404)

    return jsonify(account.to_dict())


@app_views.route('/account_balance/<account_id>', methods=['GET'], strict_slashes=False)
def get_account_balance(account_id):
    """ Retrieves a balance of an account """
    account = storage.get("Account", account_id)
    if not account:
        abort(404)
    res = [account.amount_account]
    return jsonify(res)


@app_views.route('/accounts', methods=['POST'], strict_slashes=False)
def post_account():
    """
    Creates an account
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'account_number' not in request.get_json():
        abort(400, description="Missing account number")
    if 'user_id' not in request.get_json():
        abort(400, description="Missing id of the user who is created")

    data = request.get_json()
    instance = Account(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/accounts/<account_id>', methods=['PUT'], strict_slashes=False)
def put_account(account_id):
    """
    Updates a account
    """
    account = storage.get("Account", account_id)

    if not account:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'account_number', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(account, key, value)
    storage.save()
    return make_response(jsonify(account.to_dict()), 200)


@app_views.route('/accounts/<account_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_account(account_id):
    """
    Deletes an account Object
    """

    account = storage.get("Account", account_id)

    if not account:
        abort(404)

    storage.delete(account)
    storage.save()

    return make_response(jsonify({}), 200)

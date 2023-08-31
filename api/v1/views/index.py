#!/usr/bin/python3
"""This file that return the status of the API"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    """return the status of the API"""
    return (jsonify({"status": "OK"}))

#!/usr/bin/python3
""" Blueprint for flask doc"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.Users import *
from api.v1.views.accounts import *
from api.v1.views.transactions import *

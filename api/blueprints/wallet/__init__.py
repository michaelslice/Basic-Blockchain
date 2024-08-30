# Blueprint initialization
from flask import Flask, request, Blueprint

wallet_bp = Blueprint('wallet', __name__,)

from . import routes
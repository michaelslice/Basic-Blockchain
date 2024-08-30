# Blueprint initialization
from flask import Blueprint

mempool_bp = Blueprint('mempool', __name__,)

from . import routes
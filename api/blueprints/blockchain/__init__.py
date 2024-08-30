# Blueprint initialization
from flask import Blueprint

blockchain_bp = Blueprint('blockchain', __name__,)

from . import routes
# Routes related to mempool
from flask import Flask, request
from . import mempool_bp
import hashlib
import random

@mempool_bp.route('/mempool', methods=['GET', 'POST'])
def mempool():

    data = request.get_json()

    return 'mempool'
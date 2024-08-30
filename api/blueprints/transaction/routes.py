# Routes related to transaction
from flask import Flask, request
from . import transaction_bp
import hashlib
import random

@transaction_bp.route('/transaction', methods=['POST'])
def transaction():
    if request.method == "POST":
        print("TEST")
    else:
        return {"Error": "Invalid Request"}, 400     
    
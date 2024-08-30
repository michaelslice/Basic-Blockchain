# Routes related to blockchain
from flask import Flask, request
from . import blockchain_bp
import hashlib
import random

@blockchain_bp.route('/blockchain', methods=['GET', 'POST'])
def blockchain():
    if request.method == 'GET':
        return 'test'
    else:
        return 'blockchain'
# Routes related to transaction
from flask import Flask, request, jsonify
from . import transaction_bp
import hashlib
import random
import json 

@transaction_bp.route('/transaction', methods=['POST'])
def transaction():
    
    data = request.get_json()
    
    # User1 wallet info
    User1PrivateKey = data.get("User1-Private-Key")
    User1PublicKey = data.get("User1-Public-Key")
    User1Bitcoin = data.get("User1-Bitcoin")
    
    # User2 wallet info
    User2PrivateKey = data.get("User2-Private-Key")
    User2PublicKey = data.get("User2-Public-Key")
    User2Bitcoin = data.get("User2-Bitcoin")
    
    if 
    
    
    
    
    return jsonify(data)     
    
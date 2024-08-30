"""
app.py specifies all the endpoints for the api
"""
from flask import Flask, request
import hashlib
import random
from blueprints.blockchain import blockchain_bp
from blueprints.transaction import transaction_bp
from blueprints.wallet import wallet_bp

# Create an instance of the Flask class
def create_app():
    app = Flask(__name__)
    
    # app.config.from_object(Config)
    app.register_blueprint(blockchain_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(wallet_bp)

    return app
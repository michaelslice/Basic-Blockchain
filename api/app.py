"""
app.py specifies all the endpoints for the api
"""

from flask import Flask, request
import hashlib

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/')
def home():
    return 'test'

@app.route('/transaction', method=['POST'])
def transaction():
    if request.method == "POST":
        print("TEST")
    else:
        return {"Error": "Invalid Request"}, 400     
    

@app.route('/blockchain', methods=['GET', 'POST'])
def blockchain():
    if request.method == 'GET':
        return 'test'
    else:
        return 'blockchain'


@app.route('/mine')
def node():
    return 'node'

'''
Users can make a GET request and they will retrive their public and private key info
'''
@app.route('/wallet', method=["GET"])
def node()->dict:
    
    secp256k1 = x**3
    
    
    public_key = 
    private_key = 
    
    wallet_info = {
        "public_key" : public_key,
        "private_key" : private_key,
    }
    
    return wallet_info



'''
Verify the transaction and add a new block to the blockchain
'''
@app.route('/proof-of-work')
def proofofwork():
    
    
    return 'node'

# Run the app if this script is executed 'python app.py'
if __name__ == '__main__':
    app.run(debug=True)
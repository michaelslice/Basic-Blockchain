# Routes related to transaction
from flask import Flask, request
from . import transaction_bp

@transaction_bp.route('/transaction', methods=['POST'])
def transaction()->dict:
    
    data = request.get_json()
    
    # User1 wallet info
    User1PrivateKey = data.get("User1-Private-Key")
    User1PublicKey = data.get("User1-Public-Key")
    User1Bitcoin = int(data.get("User1-Bitcoin"))
    User1BitcoinBought = int(data.get("User1-Bitcoin-Bought"))
    
    # User2 wallet info
    User2PrivateKey = data.get("User2-Private-Key")
    User2PublicKey = data.get("User2-Public-Key")
    User2Bitcoin = int(data.get("User2-Bitcoin"))
    User2BitcoinSent = int(data.get("User2-Bitcoin-Sent"))
     
    if User2BitcoinSent > User2Bitcoin or User1BitcoinBought > User2Bitcoin:
        return {"Failure": "Not enough bitcoin to conduct transaction"},400 
    else:        
        
        User2Bitcoin -= int(User2BitcoinSent)
        User1Bitcoin += int(User2BitcoinSent)
        
        transaction_details = {
            "User1-Private-Key" : User1PrivateKey,
            "User1-Public-Key" : User1PublicKey,
            "User1-Bitcoin" : User1Bitcoin,
            
            "User2-Private-Key" : User2PrivateKey,
            "User2-Public-Key" : User2PublicKey,
            "User2-Bitcoin" : User2Bitcoin,
        }
        
    return transaction_details     
    
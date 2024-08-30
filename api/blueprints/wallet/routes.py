# Routes related to wallet
from flask import Flask, request, jsonify
import hashlib
import random
from . import wallet_bp

def mod_inv(a, p):
    # Return the modular inverse of a under modulo p
    return pow(a, -1, p)

def elliptic_curve_add(p1, p2, a, p) -> tuple:
    # Add two points on the elliptic curve
    if p1 == (0, 0):
        return p2
    if p2 == (0, 0):
        return p1
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 and y1 == y2:
        # Use tangent formula
        m = (3 * x1**2 + a) * mod_inv(2 * y1, p) % p
    else:
        # Use the line formula
        m = (y2 - y1) * mod_inv(x2 - x1, p) % p
    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_multiply(k, point, a, p):
    # Multiply a point by a scalar on an elliptic curve
    result = (0, 0)
    addend = point
    while k:
        if k & 1:
            result = elliptic_curve_add(result, addend, a, p)
        addend = elliptic_curve_add(addend, addend, a, p)
        k >>= 1
    return result

'''
Users can make a GET request and they will retrive their public and private key info
'''
@wallet_bp.route('/wallet', methods=["GET"])
def wallet() -> dict:
    # Generate a random 64-bit hexadecimal string
    rand = random.randrange(10**80)
    private_key = "%064x" % rand
    private_key = int(private_key[:64], 16)  # Convert to integer
    print(f"Private Key: {private_key}")
    
    # Curve parameters for secp256k1
    G_x = int("0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F817", 16)
    G_y = int("0x483ADA7726A3C4655DA4FBFC0E1108A8FD17D448A68554199C47D08F4E7D3", 16)
    G = (G_x, G_y)
    p = int("0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F", 16)
    a = 0
    b = 7
    
    public_key = scalar_multiply(private_key, G, a, p)
    
    wallet_info = {
        "public_key": public_key,
        "private_key": private_key,
    }
    print(wallet_info)
    
    return jsonify(wallet_info)
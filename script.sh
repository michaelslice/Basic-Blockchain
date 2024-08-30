#!/bin/bash

# Flask API for generating public and private keys
url="http://127.0.0.1:5000/wallet"

# Get User 1's Public and Private Keys
response=$(curl "$url")
user1_public_key=$(echo "$response" | jq -r '.private_key')  
user1_private_key=$(echo "$response" | jq -r '.public_key | join(",")')
echo "User 1 Private Key $user1_private_key"
echo "User 1 Public Key $user1_public_key"

# Get User 2's Public and Private Keys
response=$(curl "$url")
user2_public_key=$(echo "$response" | jq -r '.private_key')  
user2_private_key=$(echo "$response" | jq -r '.public_key | join(",")')
echo "User 2 Private Key $user2_private_key"
echo "User 2 Public Key $user2_public_key"

# Conduct a transaction between them
transaction_url="http://127.0.0.1:5000/transaction"

curl -X POST $transaction_url \
    -H "Content-Type: application/json" \
    -d "{
            \"User1-Public-Key\": \"$user1_public_key\", 
            \"User1-Private-Key\": \"$user1_private_key\", 
            \"User2-Public-Key\": \"$user2_public_key\", 
            \"User2-Private-Key\": \"$user2_private_key\",
            \"User1-Bitcoin\": \"43\",
            \"User2-Bitcoin\": \"62\",
            \"User1-Bitcoin-Bought\": \"16\",
            \"User2-Bitcoin-Sent\": \"16\"
        }"
    
# If transaction is successful add transaction to the mempool
mempool_url="http://127.0.0.1:5000/mempool"

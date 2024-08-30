#!/bin/bash

url="http://100.110.149.130:5000/wallet"

response=$(curl "$url")
echo "$response"


user1_public_key=$(echo "$response" | jq -r '.private_key')  
user1_private_key=$(echo "$response" | jq -r '.public_key | join(",")')

# user2_public_key = 
# user2_private_key = 

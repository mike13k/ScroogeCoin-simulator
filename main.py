"""
In this project, we will design a cryptocurrency similar to ScroogeCoin. 

- A network of 100 users will simulate the transaction processes.

- Initially each user will have 10 ScroogCoins.

- As long as the system is running, a random transaction with random amount
  (within the range of amount the user has) will be created from User A to
  User B.

- The transaction is signed by the private-key of the sender.

- Scrooge get notified by every transaction.
- Scrooge verifies the signature before accumulating the transaction.

- Once Scrooge accumulates 10 transaction, he can form a block and attach it to 
  the blockchain.

- You are allowed to use predefined hash and digital signature libraries.
  Mention which libraries you used.
"""
from Scrooge import Scrooge
from User import User
from Ledger import Ledger

import keyboard
import random 


def run_simulation(DEBUG_MODE):
    blockchain = Scrooge()
    users = []
    for i in range(10):
        user = User()
        users.append(user)
    
    vks = [user.vk for user in users]

    # TODO - MOVED FROM SCROOGE - Create the initial coins
    print('Start - 0 coins per users\n----------------------------------\n')
    for user in users:
        print(user.vk + ':\t' + str(len(blockchain.ledger._users_coins[user.vk])))
        print('----------------------------------')
    print('\n----------------------------------\n')
    print('The initial 10 coin transactions\n----------------------------------\n')
    for vk in vks:
        blockchain.create_coin_transaction(vk, 10)
    print('\n----------------------------------\n')
    print('Inital amount of coins per user\n----------------------------------\n')
    for user in users:
        print(user.vk + ':\n' + str(len(blockchain.ledger._users_coins[user.vk])))
    print('\n----------------------------------\n')
    print('START SIMULATION')
    print('\n----------------------------------\n')

    while(True):
        if DEBUG_MODE:
            print("DEBUG MODE: Press Enter for next step")
        while DEBUG_MODE:
            if keyboard.is_pressed('\n'):
                break
            if keyboard.is_pressed(' '):
                print('Space is pressed')
                return
        else:
            if keyboard.is_pressed(' '):
                print('Space is pressed')
                return
        sender = random.choice(users)
        sender_vk = sender.vk
        while True:
            recipient = random.choice(vks) 
            if sender_vk != recipient:
                break
        if len(blockchain.ledger._users_coins[sender_vk]) >= 1:
            amount = random.randint(1, len(blockchain.ledger._users_coins[sender_vk]))
            transaction = sender.pay(amount, recipient)
            if transaction:
                blockchain.handle_payment_transaction(transaction)



if __name__ == '__main__':
    run_simulation(DEBUG_MODE=True)
    
    
# General Notes

#------ TODO
# 8- Scrooge will create and sign the 10 initial scrooge coins for each user.
# 9- A user cannot confirm a transaction unless it is published on the blockchain.
# 10- Additional transaction verification should be applied using the Merkel Tree.

#------ DONE
# 1- Each coin should have a coin ID. 
# 2- Each transaction should have a transaction ID, a hash pointer to the
# previous. transaction, the amount of coins and signed by the sender.
# 3- Each block in the blockchain should have a block ID, 10 valid
# transactions, a hash of the block, and a hash pointer to the previous block.
# 4- The final hash pointer should be signed by Scrooge.
# 5- Scrooge verifies that the transaction belongs to the owner.
# 6- Scrooge verifies that the transaction is not a Double spending.
# 7- If 5 and 6 are verified Scrooge publishes the transaction to the block.





#  Deliverables


#  ---- Some distributed over files

# ❖ A simulation of the network, with multiple users and the randomized
# process of making a transaction, making each transaction reach an arbitrary user.


# ❖ For digital signature, use any of the technique described throughout the course.

# ❖ Implement Merkel Tree for the blockchain you create. The Merkel Tree
# should reflect the change in the blockchain when adding a new block to
# the blockchain.
# ❖ Transaction verification using Merkel Tree to make sure that the coins
# are not spent before by the same user.


# Output Format

# ❖ Print initially the public key and the amount of coins for each user.
# ❖ Scoorge should print the block under construction for each new
# transaction added (include the transaction details).
# ❖ Print the blockchain after a new block is appended.
# ❖ Terminate the code using the key ‘Space’.
# ❖ Save all the printed data to a text file upon termination


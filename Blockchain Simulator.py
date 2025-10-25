//a simple blockchain simulator, ifo can be hanged to your liking 

import hashlib
import datetime
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        to_hash = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(to_hash.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, str(datetime.datetime.now()), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        last_block = self.get_latest_block()
        new_block = Block(len(self.chain), str(datetime.datetime.now()), new_data, last_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
#  Running the Blockchain Demo 
mychain = Blockchain()
mychain.add_block("John sent 100 BTC to Alex")
mychain.add_block("Alex sent 50 BTC to Joe")

for block in mychain.chain:
    print(json.dumps({
        "index": block.index,
        "timestamp": block.timestamp,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "hash": block.hash
    }, indent=4))

print("\nBlockchain valid?:", mychain.is_chain_valid())
